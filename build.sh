#!/usr/bin/env bash

set -euo pipefail

project_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$project_root"

usage() {
  printf '用法: %s [build|watch|release|clean]\n' "${0##*/}"
  printf '  build    增量编译，使用快速无损压缩（默认）\n'
  printf '  watch    监听文件变化并增量编译，不打开新窗口\n'
  printf '  release  完整内容、高压缩 PDF，适合分发\n'
  printf '  clean    清除构建缓存；日常改稿无需执行\n'
}

require_latexmk() {
  if ! command -v latexmk >/dev/null 2>&1; then
    printf '错误：未找到 latexmk，请先安装包含 XeLaTeX 的 TeX Live。\n' >&2
    exit 1
  fi
}

font_link_names=(
  SourceHanSerifCN-Regular.otf
  SourceHanSerifCN-Bold.otf
  SourceHanSansSC-Regular.otf
  SourceHanSansSC-Bold.otf
  LXGWWenKai-Regular.ttf
  LXGWWenKai-Medium.ttf
  LXGWWenKaiMono-Regular.ttf
)

font_search_roots=(
  "${HOME}/Library/Fonts"
  /Library/Fonts
  /System/Library/Fonts
  "${HOME}/.local/share/fonts"
  "${HOME}/.fonts"
  /usr/local/share/fonts
  /usr/share/fonts
)

find_font_file() {
  local pattern="$1"
  local font_root
  local font_file

  for font_root in "${font_search_roots[@]}"; do
    [[ -d "$font_root" ]] || continue
    font_file="$(find "$font_root" -maxdepth 4 -type f -iname "$pattern" -print -quit)"
    if [[ -n "$font_file" ]]; then
      printf '%s\n' "$font_file"
      return 0
    fi
  done
  return 1
}

link_required_font() {
  local display_name="$1"
  local pattern="$2"
  local link_name="$3"
  local font_file

  # 复用有效链接；仅首次构建、清理后或原字体被移走时重新搜索。
  if [[ -f "build/fonts/$link_name" ]]; then
    return 0
  fi

  if ! font_file="$(find_font_file "$pattern")"; then
    printf '错误：未找到字体 %s（文件模式：%s）。\n' "$display_name" "$pattern" >&2
    exit 1
  fi
  ln -sfn "$font_file" "build/fonts/$link_name"
}

prepare_fonts() {
  mkdir -p build/fonts
  link_required_font 'Source Han Serif CN Regular' 'SourceHanSerifCN-Regular*.otf' 'SourceHanSerifCN-Regular.otf'
  link_required_font 'Source Han Serif CN Bold' 'SourceHanSerifCN-Bold*.otf' 'SourceHanSerifCN-Bold.otf'
  link_required_font 'Source Han Sans SC Regular' 'SourceHanSansSC-Regular*.otf' 'SourceHanSansSC-Regular.otf'
  link_required_font 'Source Han Sans SC Bold' 'SourceHanSansSC-Bold*.otf' 'SourceHanSansSC-Bold.otf'
  link_required_font 'LXGW WenKai Regular' 'LXGWWenKai-Regular.*' 'LXGWWenKai-Regular.ttf'
  link_required_font 'LXGW WenKai Medium' 'LXGWWenKai-Medium.*' 'LXGWWenKai-Medium.ttf'
  link_required_font 'LXGW WenKai Mono Regular' 'LXGWWenKaiMono-Regular.*' 'LXGWWenKaiMono-Regular.ttf'
}

build_project() {
  require_latexmk
  prepare_fonts
  local compression="${BOOK_PDF_COMPRESSION:-1}"
  local previous_compression=""
  local latexmk_options=(-interaction=nonstopmode -halt-on-error -file-line-error)
  case "$compression" in
    [0-9]) ;;
    *) printf '错误：BOOK_PDF_COMPRESSION 必须为 0 到 9 的整数。\n' >&2; return 1 ;;
  esac
  if [[ -f build/.pdf-compression ]]; then
    previous_compression="$(cat build/.pdf-compression)"
  fi
  # latexmk 不一定因 PDF 转换命令变化而重建；显式处理模式切换。
  if [[ -f build/main.pdf && "$previous_compression" != "$compression" ]]; then
    latexmk_options+=(-g)
  fi
  latexmk \
    "${latexmk_options[@]}" \
    "$@" \
    tex/main.tex
  printf '%s\n' "$compression" > build/.pdf-compression
}

clean_project() {
  require_latexmk
  latexmk -C tex/main.tex
  rm -f build/.pdf-compression
  local font_link
  for font_link in "${font_link_names[@]}"; do
    rm -f "build/fonts/$font_link"
  done
  rmdir build/fonts 2>/dev/null || true
  rmdir build 2>/dev/null || true
}

case "${1:-build}" in
  build)
    build_project
    ;;
  watch)
    build_project
    build_project -pvc -view=none
    ;;
  release)
    export BOOK_PDF_COMPRESSION=9
    build_project
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
