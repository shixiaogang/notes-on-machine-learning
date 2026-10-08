#!/usr/bin/env bash

set -uo pipefail

project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$project_root"

failures=0

fail() {
  printf '缺失：%s\n' "$1" >&2
  failures=$((failures + 1))
}

check_file() {
  local path="$1"
  local description="$2"
  [[ -f "$path" ]] || fail "${description}（${path}）"
}

check_fixed() {
  local path="$1"
  local text="$2"
  local description="$3"
  if [[ ! -f "$path" ]] || ! grep -Fq -- "$text" "$path"; then
    fail "${description}（${path} 应包含 ${text}）"
  fi
}

check_regex() {
  local path="$1"
  local pattern="$2"
  local description="$3"
  if [[ ! -f "$path" ]] || ! grep -Eq -- "$pattern" "$path"; then
    fail "${description}（${path}）"
  fi
}

check_not_regex() {
  local path="$1"
  local pattern="$2"
  local description="$3"
  if [[ -f "$path" ]] && grep -Eq -- "$pattern" "$path"; then
    fail "${description}（${path}）"
  fi
}

check_order() {
  local path="$1"
  shift
  local previous_line=0
  local text
  local line

  for text in "$@"; do
    line="$(grep -nF -- "$text" "$path" 2>/dev/null | head -n 1 | cut -d: -f1)"
    if [[ -z "$line" ]] || ((line <= previous_line)); then
      fail "${path} 中的前页顺序应为：$*"
      return
    fi
    previous_line="$line"
  done
}

check_fixed_count() {
  local path="$1"
  local text="$2"
  local expected="$3"
  local description="$4"
  local count

  count="$(grep -Fc -- "$text" "$path" 2>/dev/null || true)"
  if [[ "$count" != "$expected" ]]; then
    fail "${description}（${path} 中 ${text} 应出现 ${expected} 次，实际 ${count} 次）"
  fi
}

check_section_paragraph_count() {
  local path="$1"
  local start="$2"
  local end="$3"
  local expected="$4"
  local description="$5"
  local start_line
  local end_line

  if [[ ! -f "$path" ]]; then
    fail "$description"
    return
  fi

  start_line="$(grep -nF -- "$start" "$path" 2>/dev/null | head -n 1 | cut -d: -f1)"
  if [[ -z "$start_line" ]]; then
    fail "$description"
    return
  fi

  end_line="$(
    grep -nF -- "$end" "$path" 2>/dev/null \
      | cut -d: -f1 \
      | awk -v start_line="$start_line" '$1 > start_line { print; exit }'
  )"
  if [[ -z "$end_line" ]]; then
    fail "$description"
    return
  fi

  if grep -Eq '\\par([^[:alpha:]]|$)' \
    < <(sed -n "$((start_line + 1)),$((end_line - 1))p" "$path"); then
    fail "$description"
    return
  fi

  if ! sed -n "$((start_line + 1)),$((end_line - 1))p" "$path" \
    | awk -v expected="$expected" '
      /^[[:space:]]*$/ {
        in_paragraph = 0
        next
      }
      !in_paragraph {
        paragraphs += 1
        in_paragraph = 1
      }
      END {
        exit paragraphs == expected ? 0 : 1
      }
    '; then
    fail "$description"
  fi
}

check_block_fixed() {
  local path="$1"
  local start="$2"
  local end="$3"
  local text="$4"
  local description="$5"
  local start_line
  local end_line
  local line
  local matched=false

  if [[ ! -f "$path" ]]; then
    fail "$description"
    return
  fi

  start_line="$(grep -nF -- "$start" "$path" 2>/dev/null | head -n 1 | cut -d: -f1)"
  if [[ -z "$start_line" ]]; then
    fail "$description"
    return
  fi

  end_line="$(
    grep -nF -- "$end" "$path" 2>/dev/null \
      | cut -d: -f1 \
      | awk -v start_line="$start_line" '$1 > start_line { print; exit }'
  )"
  if [[ -z "$end_line" ]]; then
    fail "$description"
    return
  fi

  while IFS= read -r line; do
    if [[ "$line" == *"$text"* ]]; then
      matched=true
      break
    fi
  done < <(sed -n "${start_line},${end_line}p" "$path")

  if [[ "$matched" != true ]]; then
    fail "$description"
  fi
}

check_block_fixed_count() {
  local path="$1"
  local start="$2"
  local end="$3"
  local text="$4"
  local expected="$5"
  local description="$6"
  local start_line
  local end_line
  local line
  local count=0

  if [[ ! -f "$path" ]]; then
    fail "$description"
    return
  fi

  start_line="$(grep -nF -- "$start" "$path" 2>/dev/null | head -n 1 | cut -d: -f1)"
  if [[ -z "$start_line" ]]; then
    fail "$description"
    return
  fi

  end_line="$(
    grep -nF -- "$end" "$path" 2>/dev/null \
      | cut -d: -f1 \
      | awk -v start_line="$start_line" '$1 > start_line { print; exit }'
  )"
  if [[ -z "$end_line" ]]; then
    fail "$description"
    return
  fi

  while IFS= read -r line; do
    if [[ "$line" == *"$text"* ]]; then
      count=$((count + 1))
    fi
  done < <(sed -n "${start_line},$((end_line - 1))p" "$path")

  if [[ "$count" != "$expected" ]]; then
    fail "${description}（应为 ${expected} 项，实际 ${count} 项）"
  fi
}

check_reference_category() {
  local path="$1"
  local start="$2"
  local end="$3"
  local expected="$4"
  local description="$5"
  shift 5
  local title

  check_block_fixed_count "$path" "$start" "$end" '\item ' "$expected" "$description"
  for title in "$@"; do
    check_block_fixed \
      "$path" \
      "$start" \
      "$end" \
      "$title" \
      "${description}，且应包含 ${title}"
  done
}

check_reference_item_descriptions() {
  local path="$1"
  local start="$2"
  local end="$3"
  local expected="$4"
  local description="$5"

  if ! awk -v start="$start" -v end="$end" -v expected="$expected" '
      BEGIN {
        valid = 1
      }
      index($0, start) {
        in_references = 1
        next
      }
      in_references && index($0, end) {
        if (in_item && item !~ /适合/) {
          valid = 0
        }
        found_end = 1
        in_references = 0
        next
      }
      in_references && /^[[:space:]]*\\item / {
        if (in_item && item !~ /适合/) {
          valid = 0
        }
        item = $0
        in_item = 1
        count += 1
        next
      }
      in_references && in_item {
        item = item "\n" $0
      }
      END {
        exit found_end && valid && count == expected ? 0 : 1
      }
    ' "$path"; then
    fail "$description"
  fi
}

check_bib_entry_fixed() {
  local path="$1"
  local key="$2"
  local text="$3"
  local description="$4"
  local entry

  entry="$(
    awk -v marker="{$key," '
      /^@/ {
        if (in_entry) {
          exit
        }
        in_entry = index($0, marker) > 0
      }
      in_entry {
        print
      }
    ' "$path"
  )"
  if [[ -z "$entry" ]] || [[ "$entry" != *"$text"* ]]; then
    fail "${description}（${path} 的 ${key} 条目应包含 ${text}）"
  fi
}

check_make_target() {
  local target="$1"
  local command="$2"
  if ! awk -v target="$target:" -v command="$command" '
      $0 == target { in_target = 1; next }
      in_target && /^[^	]/ { exit }
      in_target && substr($0, 2) == command { found = 1 }
      END { exit found ? 0 : 1 }
    ' Makefile; then
    fail "Makefile $target 入口应调用 $command"
  fi
}

check_command_error() {
  local description="$1"
  local pattern="$2"
  shift 2
  local output

  if output="$("$@" 2>&1)"; then
    fail "$description 应返回非零状态"
    return
  fi
  if ! grep -Eq -- "$pattern" <<<"$output"; then
    printf '命令错误输出：\n%s\n' "$output" >&2
    fail "$description 应给出可操作错误"
  fi
}

check_latexmk_tool_commands() {
  local commands
  local biber_command
  local makeindex_command

  if ! commands="$(perl -e 'do "./.latexmkrc" or die $@ || $!; print "$biber\n$makeindex\n"')"; then
    fail '应能读取 latexmk 的 Biber 与索引处理器配置'
    return
  fi

  biber_command="$(sed -n '1p' <<<"$commands")"
  makeindex_command="$(sed -n '2p' <<<"$commands")"
  [[ "$biber_command" == 'biber %O %S' ]] \
    || fail 'latexmk 应通过 PATH 解析 biber'
  [[ "$makeindex_command" == 'texindy -L general -C utf8 -M ../tex/styles/book-index.xdy %O -o %D %S' ]] \
    || fail 'latexmk 应通过 PATH 解析带项目样式的 UTF-8 texindy'
  [[ "$biber_command" != /* ]] \
    || fail 'latexmk 的 biber 配置不得使用绝对路径'
  [[ "$makeindex_command" != /* ]] \
    || fail 'latexmk 的 texindy 配置不得使用绝对路径'
}

check_term_pdfstring() {
  local output_dir
  local output

  output_dir="$(mktemp -d "${TMPDIR:-/tmp}/term-pdfstring.XXXXXX")"
  if ! output="$(
    xelatex \
      -interaction=nonstopmode \
      -halt-on-error \
      -output-directory="$output_dir" \
      tests/check-term-pdfstring.tex 2>&1
  )"; then
    printf 'PDF 字符串测试输出：\n%s\n' "$output" >&2
    fail '\term 在 PDF 字符串中应忽略排序键并仅保留显示词条'
  fi
  rm -rf "$output_dir"
}

check_index_pipeline() {
  local output_dir
  local output
  local full_base
  local volume_base
  local reliability_line
  local soundness_line

  output_dir="$(mktemp -d "${TMPDIR:-/tmp}/book-index.XXXXXX")"
  full_base="$output_dir/check-index-pipeline"
  volume_base="$output_dir/check-index-pipeline-volume"
  mkdir -p build

  if ! output="$(
    xelatex \
      -interaction=nonstopmode \
      -halt-on-error \
      -output-directory="$output_dir" \
      tests/check-index-pipeline.tex 2>&1
  )"; then
    printf '索引测试第一次 XeLaTeX 输出：\n%s\n' "$output" >&2
    fail '最小索引样例第一次 XeLaTeX 应成功'
    rm -rf "$output_dir"
    return
  fi
  if ! output="$(
    cd build
    texindy \
        -L general \
        -C utf8 \
        -M ../tex/styles/book-index.xdy \
        -o "$full_base.ind" \
        "$full_base.idx" 2>&1
  )"; then
    printf '索引测试 texindy 输出：\n%s\n' "$output" >&2
    fail '最小索引样例 texindy 应成功'
    rm -rf "$output_dir"
    return
  fi
  if ! output="$(
    xelatex \
      -interaction=nonstopmode \
      -halt-on-error \
      -output-directory="$output_dir" \
      tests/check-index-pipeline.tex 2>&1
  )"; then
    printf '索引测试第二次 XeLaTeX 输出：\n%s\n' "$output" >&2
    fail '最小索引样例第二次 XeLaTeX 应读取索引并生成 PDF'
    rm -rf "$output_dir"
    return
  fi

  if ! output="$(
    xelatex \
      -interaction=nonstopmode \
      -halt-on-error \
      -output-directory="$output_dir" \
      tests/check-index-pipeline-volume.tex 2>&1
  )"; then
    printf '单卷索引测试第一次 XeLaTeX 输出：\n%s\n' "$output" >&2
    fail '单卷索引样例第一次 XeLaTeX 应成功'
    rm -rf "$output_dir"
    return
  fi
  if ! output="$(
    cd build
    texindy \
        -L general \
        -C utf8 \
        -M ../tex/styles/book-index.xdy \
        -o "$volume_base.ind" \
        "$volume_base.idx" 2>&1
  )"; then
    printf '单卷索引测试 texindy 输出：\n%s\n' "$output" >&2
    fail '单卷索引样例 texindy 应成功'
    rm -rf "$output_dir"
    return
  fi
  if ! output="$(
    xelatex \
      -interaction=nonstopmode \
      -halt-on-error \
      -output-directory="$output_dir" \
      tests/check-index-pipeline-volume.tex 2>&1
  )"; then
    printf '单卷索引测试第二次 XeLaTeX 输出：\n%s\n' "$output" >&2
    fail '单卷索引样例第二次 XeLaTeX 应读取索引并生成 PDF'
    rm -rf "$output_dir"
    return
  fi

  check_fixed "$full_base.idx" \
    '机器学习@机器学习，machine learning|hyperpage' \
    '中文词条应以原词排序并在索引显示英文'
  check_fixed "$full_base.idx" \
    'SVM@SVM，support vector machine|hyperpage' \
    '缩写词条应在索引显示英文全称'
  check_fixed "$full_base.idx" \
    'k近邻@$k$近邻，$k$-nearest neighbors|hyperpage' \
    '显式排序键应保留且英文只进入显示项'
  check_fixed "$full_base.idx" \
    'R-hat diagnostic|hyperpage' \
    '含数学宏词条应在写入索引前查到英文映射'
  check_fixed "$full_base.idx" \
    'Gaussian process@Gaussian process|hyperpage' \
    '未登记纯英文词条应原样写入索引'
  check_fixed "$full_base.idx" \
    '可靠性@可靠性，reliability|hyperpage' \
    '同形词默认语义应使用首次出现的英文'
  check_fixed "$full_base.idx" \
    '可靠性-pgm-soundness@可靠性，soundness|hyperpage' \
    '同形词显式语义应生成独立英文索引项'
  check_fixed "$full_base.idx" \
    '观测完整@观测完整，complete observed data|hyperpage' \
    '“观测完整”应表达观测字段无缺失'
  check_fixed "$full_base.idx" \
    '基于分布估计的参数学习@基于分布估计的参数学习，Bayesian parameter learning|hyperpage' \
    '“基于分布估计的参数学习”应使用领域通行名称'
  check_fixed "$full_base.idx" \
    '分布估计@分布估计，posterior inference|hyperpage' \
    '参数学习语境中的“分布估计”应表达参数后验推断'
  reliability_line="$(
    grep -nF '\item 可靠性，reliability' "$full_base.ind" \
      | head -n 1 \
      | cut -d: -f1
  )"
  soundness_line="$(
    grep -nF '\item 可靠性，soundness' "$full_base.ind" \
      | head -n 1 \
      | cut -d: -f1
  )"
  if [[ -z "$reliability_line" ]] \
    || [[ -z "$soundness_line" ]] \
    || ((soundness_line != reliability_line + 1)); then
    fail '同形异义索引项应相邻并保持默认语义在前'
  fi
  check_not_regex "$full_base.idx" \
    'Gaussian process，Gaussian process' \
    '未登记纯英文词条不应重复自身'
  check_not_regex "$full_base.idx" \
    '前页哨兵词' \
    '前页词条不应进入主题词索引'
  check_not_regex "$volume_base.idx" \
    'R-hat diagnostic' \
    '单卷索引不应因载入完整词典而包含其他卷词条'
  check_fixed_count "$full_base.ind" \
    '\item 机器学习，machine learning' \
    1 \
    '重复中文词条应合并为一个索引项'
  check_regex "$full_base.ind" \
    '机器学习，machine learning，\\hyperpage\{1\}，\\hyperpage\{2\}' \
    '重复词条页码应合并并使用全角逗号分隔'
  check_not_regex "$full_base.ind" \
    ',[[:space:]]*\\hyperpage' \
    '索引项与页码及多页页码之间不应使用半角逗号'
  check_fixed "$full_base.ind" \
    '\hyperpage{' \
    'texindy 样式应保留 hyperpage'
  [[ -s "$full_base.pdf" ]] \
    || fail '最小索引样例应生成非空 PDF'
  [[ -s "$volume_base.pdf" ]] \
    || fail '单卷索引样例应生成非空 PDF'

  rm -rf "$output_dir"
}

check_cross_volume_refs() {
  local tex_files=()
  local labels_file
  local refs_file
  local cross_refs_file
  local count

  while IFS= read -r path; do
    tex_files+=("$path")
  done < <(find tex -type f -path 'tex/0[1-6]-*/*.tex' -print | sort)

  labels_file="$(mktemp "${TMPDIR:-/tmp}/book-labels.XXXXXX")"
  refs_file="$(mktemp "${TMPDIR:-/tmp}/book-refs.XXXXXX")"
  cross_refs_file="$(mktemp "${TMPDIR:-/tmp}/book-cross-refs.XXXXXX")"

  perl -ne '
    while (/\\label\{([^}]+)\}/g) {
      print "$1\t$ARGV\t$.\n";
    }
    close ARGV if eof;
  ' "${tex_files[@]}" > "$labels_file"
  perl -ne '
    while (/\\(?:ref|eqref|pageref|autoref|nameref|cref|Cref)\{([^}]+)\}/g) {
      print "$1\t$ARGV\t$.\n";
    }
    close ARGV if eof;
  ' "${tex_files[@]}" > "$refs_file"

  awk -F '\t' '
    FNR == NR {
      label_file[$1] = $2;
      next;
    }
    {
      reference_volume = $2;
      sub("^tex/", "", reference_volume);
      sub("/.*", "", reference_volume);
      target_volume = label_file[$1];
      sub("^tex/", "", target_volume);
      sub("/.*", "", target_volume);
      if (label_file[$1] != "" && reference_volume != target_volume) {
        print $1 "\t" $2 ":" $3 "\t" label_file[$1];
      }
    }
  ' "$labels_file" "$refs_file" > "$cross_refs_file"

  count="$(wc -l < "$cross_refs_file" | tr -d ' ')"
  if ((count > 0)); then
    printf '未包装的跨卷引用：\n' >&2
    cat "$cross_refs_file" >&2
    fail "所有跨卷引用应使用范围感知宏（共 $count 处）"
  fi

  rm -f "$labels_file" "$refs_file" "$cross_refs_file"
}

volume_slugs=(
  01-mathematical-preliminaries
  02-foundations
  03-models
  04-paradigms
  05-applications
  06-systems
)
volume_titles=(
  数学准备
  基础、理论和可信性
  模型
  范式
  应用
  系统
)
volume_english_titles=(
  'Mathematical Preliminaries'
  'Foundations, Theory and Trustworthiness'
  Models
  'Learning Paradigms'
  Applications
  'Machine Learning Systems'
)

check_file tex/main.tex '全集入口'
for slug in "${volume_slugs[@]}"; do
  check_file "tex/$slug/main.tex" "单卷入口 $slug"
done

expected_outputs=(
  build/main.pdf
  build/01-mathematical-preliminaries.pdf
  build/02-foundations.pdf
  build/03-models.pdf
  build/04-paradigms.pdf
  build/05-applications.pdf
  build/06-systems.pdf
)
for output in "${expected_outputs[@]}"; do
  check_fixed build.sh "$output" "构建产物 $output"
done

check_regex build.sh '(^|[[:space:]|])build\)' 'build.sh build 命令'
check_regex build.sh '(^|[[:space:]|])volume\)' 'build.sh volume <slug> 命令'
check_regex build.sh '(^|[[:space:]|])volumes\)' 'build.sh volumes 命令'
check_regex build.sh '(^|[[:space:]|])all\)' 'build.sh all 命令'
check_make_target build './build.sh build'
check_make_target volume './build.sh volume $(VOLUME)'
check_make_target volumes './build.sh volumes'
check_make_target all './build.sh all'
check_make_target test './tests/check-index-terms.sh'
check_command_error \
  'volume 缺少卷名' \
  '缺少卷名.*01-mathematical-preliminaries' \
  ./build.sh volume
check_command_error \
  'volume 未知卷名' \
  '未知卷名.*not-a-volume.*01-mathematical-preliminaries' \
  ./build.sh volume not-a-volume

check_file tex/book.tex '共享文档驱动'
check_file tex/frontmatter.tex '共享前页入口'
check_file tex/backmatter.tex '共享后页入口'
check_fixed tex/preamble.tex \
  '\newcommand{\BookSubtitle}{理论、模型和范式}' \
  '全集封面第二行使用“理论、模型和范式”'
check_block_fixed \
  tex/preamble.tex \
  '\newcommand{\BookCoverSecondLine}' \
  '\newcommand{\BookAuthor}' \
  '\ifBookVolumeEdition' \
  '封面第二行按全集与单卷模式切换'
check_block_fixed \
  tex/preamble.tex \
  '\newcommand{\BookCoverSecondLine}' \
  '\newcommand{\BookAuthor}' \
  '\BookSubtitle' \
  '全集封面第二行复用 BookSubtitle'
check_block_fixed \
  tex/preamble.tex \
  '\newcommand{\BookCoverSecondLine}' \
  '\newcommand{\BookAuthor}' \
  '卷\zhnumber{\BookVolumeNumber}：\BookVolumeChineseTitle' \
  '单卷封面第二行使用“卷一：卷名”形式'
check_fixed tex/preamble.tex '\newcommand{\BookAuthor}{施晓罡}' '作者署名使用中文姓名'
check_not_regex tex/preamble.tex 'SHI XIAOGANG' '作者署名不应保留全大写拼音'
check_fixed tex/preamble.tex \
  '\newcommand{\BookEditionLabel}{\BookYear 年 · \BookEdition}' \
  '封面与内扉页共用年份版本标签'
check_fixed tex/preamble.tex \
  'Creative Commons Attribution-NonCommercial-NoDerivatives' \
  '版权页使用 CC BY-NC-ND 4.0 英文许可名称'
check_fixed tex/preamble.tex \
  'https://creativecommons.org/licenses/by-nc-nd/4.0/' \
  '版权页链接 CC BY-NC-ND 4.0 许可页'
check_fixed tex/preamble.tex \
  'You may not use this file except in compliance with the License.' \
  '版权页保留用户指定的英文许可句式'
check_not_regex tex/preamble.tex \
  '^[[:space:]]*you may not use this file' \
  '版权页英文句首应大写'
check_fixed tex/preamble.tex \
  'software distributed under the License is distributed on an "AS IS" BASIS,' \
  '版权页保留用户指定的免责声明'
check_not_regex tex/preamble.tex \
  'Licensed under the Apache License' \
  '版权页许可名称不应保留 Apache 2.0'
check_fixed tex/preamble.tex \
  '\usepackage[copyright=false]{ccicons}' \
  'CC 图标不得覆盖标准版权符号'
check_fixed LICENSE 'Apache License' '工程代码保留 Apache 2.0 根许可证'
check_fixed tex/book.tex '\input{tex/frontmatter}' '共享驱动载入前页'
check_fixed tex/book.tex '\input{tex/backmatter}' '共享驱动载入后页'
check_regex tex/main.tex 'BookEditionMode.*book' '全集入口声明全集模式'
check_fixed tex/main.tex '\input{tex/book}' '全集入口调用共享文档驱动'

check_file tex/frontmatter/preface.tex '共享前言'
check_file tex/frontmatter/mathematical-notation.tex '共享数学符号页'
check_order tex/frontmatter.tex \
  '\makebookcover' \
  '\makebooktitle' \
  '\makebookcopyright' \
  '\input{tex/frontmatter/preface}' \
  '\input{tex/frontmatter/mathematical-notation}' \
  '\tableofcontents'
check_fixed tex/frontmatter/preface.tex '\section*{本书目标}' '前言“本书目标”无编号小节'
check_fixed tex/frontmatter/preface.tex '\section*{本书内容}' '前言“本书内容”无编号小节'
check_fixed tex/frontmatter/preface.tex '\section*{参考资料}' '前言“参考资料”无编号小节'
check_not_regex tex/frontmatter/preface.tex '\\section\*\{参考资源\}' '前言不应保留“参考资源”标题'
check_section_paragraph_count \
  tex/frontmatter/preface.tex \
  '\section*{本书内容}' \
  '\section*{参考资料}' \
  1 \
  '前言“本书内容”应为一个连续段落'

reference_categories=(
  综合与基础
  统计学习与学习理论
  概率模型与图模型
  神经网络与深度学习
  强化学习
  应用与系统
)
for category in "${reference_categories[@]}"; do
  check_fixed tex/frontmatter/preface.tex "\\paragraph*{${category}}" "参考资料按“${category}”分类"
done
check_fixed_count tex/frontmatter/preface.tex '\begin{itemize}' 6 '参考资料每类使用一层书目列表'
check_fixed_count tex/frontmatter/preface.tex '\end{itemize}' 6 '参考资料列表应完整闭合'
check_fixed_count tex/frontmatter/preface.tex '\item ' 27 '参考资料应包含 27 个书目列表项'
check_reference_item_descriptions \
  tex/frontmatter/preface.tex \
  '\section*{参考资料}' \
  '上述教材的完整出版信息列于卷末参考文献。' \
  27 \
  '参考资料的 27 个书目项均应明确说明适合查阅的问题'
check_reference_category tex/frontmatter/preface.tex \
  '\paragraph*{综合与基础}' \
  '\paragraph*{统计学习与学习理论}' \
  5 \
  '“综合与基础”应包含 5 本书' \
  '\emph{Machine Learning}' \
  '\emph{Pattern Recognition and Machine Learning}' \
  '周志华的《机器学习》' \
  '李航的《统计学习方法（第 2 版）》' \
  '\emph{Mathematics for Machine Learning}'
check_reference_category tex/frontmatter/preface.tex \
  '\paragraph*{统计学习与学习理论}' \
  '\paragraph*{概率模型与图模型}' \
  4 \
  '“统计学习与学习理论”应包含 4 本书' \
  '\emph{The Elements of Statistical' \
  '\emph{Understanding Machine Learning:' \
  '\emph{Foundations of Machine Learning}' \
  '\emph{An Introduction to Statistical Learning}'
check_reference_category tex/frontmatter/preface.tex \
  '\paragraph*{概率模型与图模型}' \
  '\paragraph*{神经网络与深度学习}' \
  5 \
  '“概率模型与图模型”应包含 5 本书' \
  '\emph{Machine Learning: A Probabilistic Perspective}' \
  '\emph{Probabilistic Machine Learning: An Introduction}' \
  '\emph{Probabilistic Graphical Models: Principles and' \
  '\emph{Gaussian Processes for Machine Learning}' \
  '\emph{Probabilistic Machine Learning: Advanced Topics}'
check_block_fixed \
  tex/frontmatter/preface.tex \
  '\item Murphy 的 \emph{Probabilistic Machine Learning: An Introduction}' \
  '\item Murphy 的 \emph{Probabilistic Machine Learning: Advanced Topics}' \
  '适合查阅现代' \
  'Murphy《Probabilistic Machine Learning: An Introduction》应明确说明适合查阅的问题'
check_reference_category tex/frontmatter/preface.tex \
  '\paragraph*{神经网络与深度学习}' \
  '\paragraph*{强化学习}' \
  5 \
  '“神经网络与深度学习”应包含 5 本书' \
  '\emph{Deep Learning}' \
  '\emph{Deep Learning: Foundations and Concepts}' \
  '邱锡鹏的《神经网络与深度学习》' \
  '\emph{Dive into Deep Learning}' \
  '\emph{Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow}'
check_reference_category tex/frontmatter/preface.tex \
  '\paragraph*{强化学习}' \
  '\paragraph*{应用与系统}' \
  2 \
  '“强化学习”应包含 2 本书' \
  '\emph{Reinforcement Learning: An Introduction}' \
  '\emph{Algorithms for Reinforcement Learning}'
check_reference_category tex/frontmatter/preface.tex \
  '\paragraph*{应用与系统}' \
  '上述教材的完整出版信息列于卷末参考文献。' \
  6 \
  '“应用与系统”应包含 6 本书' \
  '\emph{Introduction to Information Retrieval}' \
  '\emph{Designing Machine Learning Systems}' \
  '\emph{Speech and Language Processing}' \
  '\emph{Computer Vision: Algorithms and Applications}' \
  '\emph{Recommender Systems: The Textbook}' \
  '\emph{Designing Data-Intensive Applications}'

reference_keys=(
  mitchell1997
  bishop2006
  zhou2016machinelearning
  li2019statisticallearning
  hastie2009
  shalevshwartz2014
  pgm-murphy2012
  murphy2022probabilistic
  pgm-koller2009
  rasmussen2006
  goodfellow2016
  bishop2024deep
  sutton2018
  manning2008ir
  huyen2022designing
  deisenroth2020mathematics
  mohri2018foundations
  james2021statistical
  murphy2023advanced
  qiu2020neural
  zhang2023dive
  geron2022hands-on
  szepesvari2010algorithms
  jurafsky2009speech
  szeliski2022computer
  aggarwal2016recommender
  kleppmann2026designing
)
for key in "${reference_keys[@]}"; do
  check_fixed tex/frontmatter/preface.tex "$key" "前言登记参考资料 $key"
  check_fixed tex/references.bib "{$key," "参考资料书目包含 $key"
done
check_bib_entry_fixed tex/references.bib jurafsky2009speech \
  'edition = {2}' \
  '《Speech and Language Processing》采用正式第二版'
check_bib_entry_fixed tex/references.bib jurafsky2009speech \
  'date = {2009}' \
  '《Speech and Language Processing》采用 2009 年正式版'
check_bib_entry_fixed tex/references.bib qiu2020neural \
  'date = {2020-04-20}' \
  '《神经网络与深度学习》采用 2020 年正式第一版'
check_bib_entry_fixed tex/references.bib geron2022hands-on \
  'date = {2022}' \
  '《Hands-On Machine Learning》采用 2022 年出版记录'
check_bib_entry_fixed tex/references.bib kleppmann2026designing \
  'edition = {2}' \
  '《Designing Data-Intensive Applications》采用第二版'
check_bib_entry_fixed tex/references.bib kleppmann2026designing \
  'date = {2026}' \
  '《Designing Data-Intensive Applications》采用 2026 年正式版'
check_fixed tex/references.bib \
  'title = {Probabilistic Machine Learning: An Introduction}' \
  '补充 Murphy 概率机器学习教材'
check_fixed tex/references.bib \
  'title = {Designing Machine Learning Systems}' \
  '补充机器学习系统教材'
check_fixed tex/frontmatter/mathematical-notation.tex '\chapter*{数学符号}' '数学符号无编号页'
notation_groups=(
  '\noindent{\heiti\bfseries 对象与线性代数\par}'
  '{\heiti\bfseries 微积分与优化\par}'
  '{\heiti\bfseries 概率与信息论\par}'
)
for group in "${notation_groups[@]}"; do
  check_fixed_count tex/frontmatter/mathematical-notation.tex "$group" 1 "数学符号包含唯一的 ${group} 分组"
done
check_order tex/frontmatter/mathematical-notation.tex "${notation_groups[@]}"
check_not_regex tex/frontmatter/mathematical-notation.tex \
  '概率、微积分与优化' \
  '数学符号不应合并概率、微积分与优化分组'
check_block_fixed \
  tex/frontmatter/mathematical-notation.tex \
  '\begin{fullwidth}' \
  '\begingroup' \
  '下表汇总全书反复使用的记号。各章若赋予符号更具体的含义，会在首次使用时另行说明。' \
  '数学符号页首说明应位于 fullwidth'
check_section_paragraph_count \
  tex/frontmatter/mathematical-notation.tex \
  '\begin{fullwidth}' \
  '\begingroup' \
  1 \
  '数学符号页首说明应为一个连续段落'
check_block_fixed \
  tex/frontmatter/mathematical-notation.tex \
  '下表汇总全书反复使用的记号。各章若赋予符号更具体的含义，会在首次使用时另行说明。' \
  "${notation_groups[0]}" \
  '\vspace{5mm}' \
  '数学符号页首说明与第一个分组之间应增加 5mm 间距'
object_notation_markers=(
  '\delta_{i,j}'
)
for marker in "${object_notation_markers[@]}"; do
  check_block_fixed \
    tex/frontmatter/mathematical-notation.tex \
    "${notation_groups[0]}" \
    "${notation_groups[1]}" \
    "$marker" \
    "对象与线性代数分组应包含 $marker"
done
probability_notation_markers=(
  'p(x\mid y)'
  'X\perp Y\mid Z'
  '\mathbb{E}[X]'
  '\mathcal{N}(\bm{\mu},\bm{\Sigma})'
  '\mathbb{I}\{A\}'
  '\operatorname{KL}(p\Vert q)'
  'p(\bm{x})\propto q(\bm{x})'
)
for marker in "${probability_notation_markers[@]}"; do
  check_block_fixed \
    tex/frontmatter/mathematical-notation.tex \
    "${notation_groups[2]}" \
    '\endgroup' \
    "$marker" \
    "概率与信息论分组应包含 $marker"
done
for marker in '\delta_{i,j}' 'f(n)=\mathcal{O}(g(n))'; do
  check_block_fixed_count \
    tex/frontmatter/mathematical-notation.tex \
    "${notation_groups[2]}" \
    '\endgroup' \
    "$marker" \
    0 \
    "概率与信息论分组不应包含 $marker"
done
calculus_notation_markers=(
  '\dfrac{\mathrm{d}f}{\mathrm{d}x}'
  '\nabla_{\bm{w}}L(\bm{w})'
  '\nabla_{\bm{x}}\bm{f}'
  '\nabla^{2}_{\bm{x}}f'
  '\argmin_{\bm{w}}L(\bm{w})'
  'f(n)=\mathcal{O}(g(n))'
)
for marker in "${calculus_notation_markers[@]}"; do
  check_block_fixed \
    tex/frontmatter/mathematical-notation.tex \
    "${notation_groups[1]}" \
    "${notation_groups[2]}" \
    "$marker" \
    "微积分与优化分组应包含 $marker"
done
notation_markers=(
  '\mathbb{Z}'
  '\subseteq'
  '\operatorname{tr}'
  '\bm{A}^{\dagger}'
  'p(x\mid y)'
  'p(x)=\int p(x,y)\,\mathrm{d}y'
  '\perp'
  '\operatorname{Cov}'
  '\mathcal{N}'
  '\mathbb{I}'
  '\nabla_{\bm{x}}\bm{f}'
  '\nabla^{2}'
  '\operatorname{KL}'
  '\mathcal{O}'
)
for marker in "${notation_markers[@]}"; do
  check_fixed tex/frontmatter/mathematical-notation.tex "$marker" "数学符号补充 $marker"
done
check_not_regex tex/frontmatter/preface.tex \
  '\\(addcontentsline|pdfbookmark)' \
  '前言内部不应新增目录项或 PDF 书签'
check_not_regex tex/frontmatter/mathematical-notation.tex \
  '\\(addcontentsline|pdfbookmark)' \
  '数学符号页不应在本任务新增目录项或 PDF 书签'
check_fixed tex/references.bib '@book{zhou2016machinelearning,' '周志华《机器学习》书目条目'
check_fixed tex/references.bib 'isbn = {9787302423287}' '周志华《机器学习》ISBN'
check_fixed tex/references.bib \
  'https://www.tup.com.cn/booksCenter/book_06402703.html' \
  '周志华《机器学习》官方页面'
check_fixed tex/references.bib '@book{li2019statisticallearning,' '李航《统计学习方法》书目条目'
check_fixed tex/references.bib 'isbn = {9787302517276}' '李航《统计学习方法》ISBN'
check_fixed tex/references.bib \
  'https://www.tup.tsinghua.edu.cn/booksCenter/book_08132901.html' \
  '李航《统计学习方法》官方页面'

if [[ "${BOOK_EDITION_CHECK_SCOPE:-all}" != task-5 ]]; then
  check_not_regex tex/frontmatter.tex '\\pdfbookmark(\[[^]]*\])?\{前页\}' '不应建立“前页”父书签'
  check_fixed tex/frontmatter.tex '\BookTopBookmark{封面}' '封面 PDF 书签标识'
  check_fixed tex/frontmatter/preface.tex '\BookTopBookmark{前言}' '前言 PDF 书签标识'
  check_fixed tex/frontmatter/mathematical-notation.tex \
    '\BookTopBookmark{数学符号}' \
    '数学符号 PDF 书签标识'
  check_fixed tex/styles/structure.tex '\BookTopBookmark{\contentsname}' '目录 PDF 书签标识'
  check_fixed tex/backmatter.tex \
    '\BookBackmatterChapter{参考文献}{book-bibliography}' \
    '参考文献 PDF 书签标识'
  check_fixed tex/backmatter.tex \
    '\BookBackmatterIndexChapter{#1}' \
    '索引 PDF 书签标识'
fi

check_fixed tex/backmatter.tex '\backmatter' '共享后页进入 backmatter'
check_fixed tex/backmatter.tex '\printbibliography' '共享后页输出参考文献'
check_fixed tex/backmatter.tex '\renewcommand{\indexname}{索引}' '共享后页恢复中文索引标题'
check_fixed tex/backmatter.tex '\printindex' '共享后页输出索引'
check_not_regex tex/backmatter.tex '\\nocite\{\\?\*\}' '共享后页不得输出未引用文献'
check_block_fixed \
  tex/styles/layout.tex \
  '\renewenvironment{theindex}' \
  '\makeatother' \
  '\begin{multicols}{2}' \
  '双语索引应使用两栏排版'
check_fixed tex/preamble.tex '\usepackage{makeidx}' '载入主题词索引支持'
check_fixed tex/preamble.tex '\makeindex' '建立主题词索引'
check_fixed tex/preamble.tex '\input{tex/index-terms}' '共享导言载入索引词典总入口'
check_regex tex/styles/fonts.tex \
  '\\NewDocumentCommand\{\\term\}\{o m\}' \
  '\term 支持可选排序键'
check_fixed tex/styles/fonts.tex '\if@mainmatter' '\term 仅在正文阶段写入索引'
check_file tex/index-terms.tex '索引词典总入口'
for slug in "${volume_slugs[@]}"; do
  check_file "tex/index-terms/$slug.tex" "索引词典分片 $slug"
  check_fixed tex/index-terms.tex \
    "\\input{tex/index-terms/$slug}" \
    "索引词典总入口载入 $slug 分片"
done
check_latexmk_tool_commands
check_index_pipeline
check_term_pdfstring
check_cross_volume_refs
check_fixed tex/02-foundations/01-basics/02-machine-learning-models.tex \
  '\term[k近邻]{$k$近邻}' \
  '数学开头词条使用稳定排序键'
check_block_fixed \
  tex/styles/layout.tex \
  '\newcommand{\bookvolumetitlepage}' \
  '% 分部首页' \
  '\fill[BookInk]' \
  '卷首页应使用 BookInk 深色背景'
check_block_fixed \
  tex/styles/layout.tex \
  '\newcommand{\makebookcover}' \
  '\newcommand{\makebooktitle}' \
  '\BookCoverSecondLine' \
  '封面使用统一的第二行宏'
check_block_fixed \
  tex/styles/layout.tex \
  '\newcommand{\makebooktitle}' \
  '\newcommand{\makebookcopyright}' \
  '\fontsize{34}{42}\selectfont\BookTitle' \
  '内扉页中文书名应与封面使用相同字号'
check_block_fixed \
  tex/styles/layout.tex \
  '\newcommand{\makebooktitle}' \
  '\newcommand{\makebookcopyright}' \
  '\fontsize{18}{24}\selectfont\BookCoverSecondLine' \
  '内扉页第二行应与封面使用相同字号和内容宏'
check_block_fixed \
  tex/styles/layout.tex \
  '\newcommand{\makebooktitle}' \
  '\newcommand{\makebookcopyright}' \
  '\vspace{6mm}' \
  '内扉页书名与第二行之间应保持 6mm 间距'
check_block_fixed \
  tex/styles/layout.tex \
  '\newcommand{\makebookcopyright}' \
  '% 目录中的卷' \
  '\ccLogo' \
  '版权页应使用大号 CC 背景图标'
check_block_fixed \
  tex/styles/layout.tex \
  '\newcommand{\makebookcopyright}' \
  '% 目录中的卷' \
  '\ccbyncnd' \
  '版权页应显示 CC BY NC ND 图标组'
check_fixed tex/styles/structure.tex \
  '\addcontentsline{toc}{bookbackmatter}{\protect\booktocbackmatterbadge{#1}}' \
  '参考文献与索引应写入专用后页目录层级'
check_not_regex tex/styles/structure.tex \
  '\\addcontentsline\{toc\}\{bookbackmatter\}\{\\protect\\numberline' \
  '后页目录标题不应放入无法点击的 numberline'
check_fixed tex/styles/structure.tex \
  '\titlecontents{bookbackmatter}[\booktoctitleindent]' \
  '后页目录条目应与部分条目使用相同缩进'
check_fixed tex/styles/structure.tex \
  '\hspace*{-25mm}' \
  '后页目录色块应回退到部分编号块的左边界'
check_not_regex tex/styles/layout.tex \
  '第\\zhnumber\{\\BookVolumeNumber\}卷' \
  '单卷封面不应再单独显示“第一卷”'
check_not_regex tex/styles/layout.tex \
  '\{\\BookVolumeChineseTitle\}' \
  '单卷封面不应再另列卷名'
check_block_fixed \
  tex/styles/structure.tex \
  '\RenewDocumentCommand{\part}' \
  '\makeatother' \
  '\fill[BookPaper]' \
  '部首页应恢复 BookPaper 浅灰背景'
check_block_fixed \
  tex/styles/structure.tex \
  '\RenewDocumentCommand{\part}' \
  '\makeatother' \
  'text=BookInk' \
  '部首页中文标题应恢复 BookInk'
check_block_fixed \
  tex/styles/structure.tex \
  '\RenewDocumentCommand{\part}' \
  '\makeatother' \
  'text=BookMuted' \
  '部首页英文标题应恢复 BookMuted'
check_fixed_count tex/styles/layout.tex '\BookEditionLabel' 2 '封面与内扉页应使用统一版本标签'
check_not_regex tex/styles/layout.tex \
  '\\BookYear/\\BookEdition' \
  '封面与内扉页不应保留斜线版本写法'
check_fixed tex/styles/layout.tex \
  '\newcommand{\bookchapterrunningtitle}' \
  '页眉定义章标题样式'
check_fixed tex/styles/layout.tex \
  '\newcommand{\booksectionrunningtitle}' \
  '页眉定义节标题样式'
check_fixed tex/styles/layout.tex \
  '\if@mainmatter\booksectionrunningtitle\else\bookchapterrunningtitle\fi' \
  '右页正文使用节页眉且前后页回退章标题'
check_fixed tex/styles/layout.tex \
  '\fancyhead[L]{\ifodd\value{page}\bookoddpagerunningtitle\else\bookpagebadge\fi}' \
  '奇数页内侧显示节标题且偶数页外侧显示页码'
check_fixed tex/styles/layout.tex \
  '\fancyhead[R]{\ifodd\value{page}\bookpagebadge\else\bookchapterrunningtitle\fi}' \
  '奇数页外侧显示页码且偶数页内侧显示章标题'
check_fixed tex/styles/layout.tex \
  '\markboth{\if@mainmatter\BookChapterName\quad\fi #1}{}' \
  '进入新章时写入章标题并清空旧节标记'
check_fixed tex/styles/layout.tex \
  '\renewcommand{\sectionmark}[1]' \
  '节标题写入右页页眉标记'
check_fixed tex/styles/layout.tex \
  '\markright{\if@mainmatter\thesection\quad\fi #1}' \
  '节页眉包含节号与节标题'
check_fixed README.md \
  '书稿正文与原创图表采用 CC BY-NC-ND 4.0' \
  'README 说明书稿内容许可'
check_fixed README.md \
  'LaTeX 样式、构建脚本、测试和代码示例继续使用 Apache License 2.0' \
  'README 说明工程代码许可'
check_fixed specs/design.md \
  '卷首页整页铺满 `BookInk`' \
  '设计规范应记录卷首页墨蓝背景'
check_fixed specs/design.md \
  '使用 `BookPaper` 浅灰整页背景和 `BookTeal` 青色编号块' \
  '设计规范应记录部首页浅灰背景'
check_fixed specs/design.md \
  '索引显示名称统一为“索引”' \
  '设计规范应记录中文索引标题'
check_fixed specs/design.md \
  '“参考资料”使用六类单层列表' \
  '设计规范应记录参考资料分类与列表结构'
check_fixed specs/design.md \
  '27 本教材通过集中 `\nocite` 显式登记' \
  '设计规范应记录前页教材登记规则'
check_fixed specs/design.md \
  '偶数页显示章号与章标题，奇数页显示节号与节标题' \
  '设计规范应记录正文奇偶页眉'
check_fixed specs/design.md \
  '年份与版本统一写作 `2026 年 · 第一版`' \
  '设计规范应记录封面版本格式'
check_fixed specs/design.md \
  '书稿正文与原创图表采用 CC BY-NC-ND 4.0' \
  '设计规范应记录书稿内容许可'
check_fixed plans/book-structure.md \
  '全集卷首页使用墨蓝实底' \
  '结构计划应记录卷首页墨蓝背景'
check_fixed plans/book-structure.md \
  '分部页使用浅灰实底、青色编号块、墨蓝粗体中文标题和灰色常规英文标题' \
  '结构计划应记录部首页恢复样式'
check_fixed plans/book-structure.md \
  '索引页、目录和 PDF 书签统一使用“索引”作为标题' \
  '结构计划应记录中文索引标题'

for index in "${!volume_slugs[@]}"; do
  slug="${volume_slugs[$index]}"
  volume_number=$((index + 1))
  entry="tex/$slug/main.tex"

  check_regex "$entry" 'BookEditionMode.*volume' "$slug 声明单卷模式"
  check_regex "$entry" "BookVolumeNumber[^[:digit:]]*$volume_number([^[:digit:]]|$)" \
    "$slug 声明局部编号所需卷号 $volume_number"
  check_fixed "$entry" "${volume_titles[$index]}" "$slug 声明中文卷名"
  check_fixed "$entry" "${volume_english_titles[$index]}" "$slug 声明英文卷名"
  check_fixed "$entry" "tex/$slug/volume" "$slug 声明卷内容入口"
  check_fixed "$entry" '\input{tex/book}' "$slug 调用共享文档驱动"
done

if ((failures > 0)); then
  printf '结构检查失败：共 %d 个缺失项。\n' "$failures" >&2
  exit 1
fi

printf '结构检查通过：全集与六个单卷接口完整。\n'
