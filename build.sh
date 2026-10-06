#!/usr/bin/env bash

set -euo pipefail

project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$project_root"

book_source=tex/main.tex
book_output=target/machine-learning-notes.pdf
volume_slugs=(
  01-mathematical-preliminaries
  02-foundations
  03-models
  04-paradigms
  05-applications
  06-systems
)
volume_sources=(
  tex/01-mathematical-preliminaries/main.tex
  tex/02-foundations/main.tex
  tex/03-models/main.tex
  tex/04-paradigms/main.tex
  tex/05-applications/main.tex
  tex/06-systems/main.tex
)
volume_outputs=(
  target/vol1-mathematical-preliminaries.pdf
  target/vol2-foundations.pdf
  target/vol3-models.pdf
  target/vol4-paradigms.pdf
  target/vol5-applications.pdf
  target/vol6-systems.pdf
)

usage() {
  printf '用法: %s [build|volume <slug>|volumes|all|check-target|watch|release|clean]\n' "${0##*/}"
  printf '  build          增量编译全集，使用快速无损压缩（默认）\n'
  printf '  volume <slug>  只编译指定单卷\n'
  printf '  volumes        依次编译六个单卷\n'
  printf '  all            依次编译全集和六个单卷\n'
  printf '  check-target   检查七份成品与正文是否一致\n'
  printf '  watch          只监听全集，不打开新窗口\n'
  printf '  release        以最高压缩等级编译全集\n'
  printf '  clean          清除全集与六个单卷的构建缓存和产物\n'
  printf '可用卷名：%s\n' "${volume_slugs[*]}"
}

require_latexmk() {
  if ! command -v latexmk >/dev/null 2>&1; then
    printf '错误：未找到 latexmk，请先安装包含 XeLaTeX 的 TeX Live。\n' >&2
    exit 1
  fi
}

# 字体随仓库分发；不搜索系统字体，也不复用旧的构建期链接。
prepare_fonts() {
  local font_file
  local required_fonts=(
    LXGWWenKai-Medium.ttf
    LXGWWenKai-Regular.ttf
    LXGWWenKaiMono-Regular.ttf
    STIXTwoText-Bold.otf
    STIXTwoText-BoldItalic.otf
    STIXTwoText-Italic.otf
    STIXTwoText-Regular.otf
    SourceCodePro-Regular.otf
    SourceCodePro-RegularIt.otf
    SourceCodePro-Semibold.otf
    SourceCodePro-SemiboldIt.otf
    SourceHanSansSC-Bold.otf
    SourceHanSansSC-Regular.otf
    SourceHanSerifCN-Bold.otf
    SourceHanSerifCN-Regular.otf
    SourceSans3-Regular.otf
    SourceSans3-RegularIt.otf
    SourceSans3-Semibold.otf
    SourceSans3-SemiboldIt.otf
    stix2-type1/type1/STIX2Math.pfb
    stix2-type1/map/stix2.map
  )
  for font_file in "${required_fonts[@]}"; do
    if [[ ! -f "fonts/$font_file" ]]; then
      printf '错误：缺少仓库字体 fonts/%s，请恢复完整的 fonts/ 目录。\n' "$font_file" >&2
      return 1
    fi
  done
}

build_entry() {
  local source="$1"
  local output="$2"
  shift 2

  require_latexmk
  prepare_fonts
  local compression="${BOOK_PDF_COMPRESSION:-1}"
  local previous_compression=""
  local output_name="${output##*/}"
  local job_name="${source#tex/}"
  job_name="${job_name%/main.tex}"
  if [[ "$source" == "$book_source" ]]; then job_name=main; fi
  local cached_pdf="build/$job_name.pdf"
  local compression_cache="build/.pdf-compression-$job_name"
  local latexmk_options=(-interaction=nonstopmode -halt-on-error -file-line-error)
  case "$compression" in
    [0-9]) ;;
    *) printf '错误：BOOK_PDF_COMPRESSION 必须为 0 到 9 的整数。\n' >&2; return 1 ;;
  esac
  if [[ -f "$compression_cache" ]]; then
    previous_compression="$(cat "$compression_cache")"
  fi
  # latexmk 不一定因 PDF 转换命令变化而重建；显式处理模式切换。
  if [[ -f "$cached_pdf" && "$previous_compression" != "$compression" ]]; then
    latexmk_options+=(-g)
  fi
  latexmk \
    "${latexmk_options[@]}" \
    -jobname="$job_name" \
    "$@" \
    "$source"
  mkdir -p target
  cp "$cached_pdf" "$output.tmp"
  mv "$output.tmp" "$output"
  printf '%s\n' "$compression" > "$compression_cache"
}

volume_index() {
  local slug="$1"
  local index
  for index in "${!volume_slugs[@]}"; do
    if [[ "${volume_slugs[$index]}" == "$slug" ]]; then
      printf '%s\n' "$index"
      return 0
    fi
  done
  return 1
}

build_volume() {
  local slug="$1"
  local index
  index="$(volume_index "$slug")"
  build_entry "${volume_sources[$index]}" "${volume_outputs[$index]}"
}

build_volumes() {
  local slug
  for slug in "${volume_slugs[@]}"; do
    build_volume "$slug"
  done
}

clean_project() {
  require_latexmk
  local index
  latexmk -C -jobname=main "$book_source"
  for index in "${!volume_slugs[@]}"; do
    latexmk -C \
      -jobname="${volume_slugs[$index]}" \
      "${volume_sources[$index]}"
  done
  rm -rf -- "$project_root/build" "$project_root/target"
}

case "${1:-build}" in
  build)
    build_entry "$book_source" "$book_output"
    ;;
  volume)
    if [[ -z "${2:-}" ]]; then
      printf '错误：volume 缺少卷名；可用卷名：%s。\n' "${volume_slugs[*]}" >&2
      exit 2
    fi
    if ! volume_index "$2" >/dev/null; then
      printf '错误：未知卷名 "%s"；可用卷名：%s。\n' "$2" "${volume_slugs[*]}" >&2
      exit 2
    fi
    build_volume "$2"
    ;;
  volumes)
    build_volumes
    ;;
  all)
    snapshot="$(mktemp "${TMPDIR:-/tmp}/book-inputs.XXXXXX")"
    trap 'rm -f "$snapshot"' EXIT
    python3 scripts/check_target_pdfs.py snapshot > "$snapshot"
    build_entry "$book_source" "$book_output"
    build_volumes
    python3 scripts/check_target_pdfs.py record --snapshot "$snapshot"
    python3 scripts/check_target_pdfs.py check
    ;;
  check-target)
    python3 scripts/check_target_pdfs.py check
    ;;
  watch)
    build_entry "$book_source" "$book_output"
    export BOOK_TARGET_PDF="$book_output"
    build_entry "$book_source" "$book_output" -pvc -view=none
    ;;
  release)
    export BOOK_PDF_COMPRESSION=9
    build_entry "$book_source" "$book_output"
    ;;
  clean)
    clean_project
    ;;
  -h|--help|help)
    usage
    ;;
  *)
    usage >&2
    exit 2
    ;;
esac
