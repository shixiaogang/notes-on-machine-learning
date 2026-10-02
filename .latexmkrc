$pdf_mode = 5;
$xelatex = 'xelatex %O %S';
$out_dir = 'build';

# 最高压缩等级会反复压缩大幅 PNG 和嵌入字体。日常使用快速无损压缩，
# release 模式通过环境变量恢复等级 9；不降低分辨率或更换字体。
my $book_compression = $ENV{'BOOK_PDF_COMPRESSION'} // '1';
die "BOOK_PDF_COMPRESSION must be an integer from 0 to 9\n"
    unless $book_compression =~ /\A[0-9]\z/;
$xdvipdfmx = "xdvipdfmx -E -z $book_compression %O -o %D %S";

# 始终优先使用 tex/styles/ 中固定版本的 Tufte-LaTeX。
$ENV{'TEXINPUTS'} = './tex//:' . ($ENV{'TEXINPUTS'} // '');
