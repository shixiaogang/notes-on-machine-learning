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
  # 兼容清理旧版本生成的字体链接；fonts/ 中的源文件不会被清除。
  if [[ -d build/fonts ]]; then
    find build/fonts -maxdepth 1 -type l -delete
    rmdir build/fonts 2>/dev/null || true
  fi
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
