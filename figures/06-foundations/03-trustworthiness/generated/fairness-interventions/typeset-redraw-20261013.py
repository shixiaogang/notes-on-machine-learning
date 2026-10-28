from pathlib import Path
import sys,json,hashlib,itertools
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'figures/06-foundations/00-shared/generated'))
from typeset_common import Typeset,run,FONT_FILES
FONT_FILES['fallback']='STIXTwoMath-Regular.otf'
t=Typeset(HERE/'background-redraw-20261013.png',HERE,ROOT/'fonts')
for y,title in [(87,'训练样本：补充采集与标签核实'),(534,'训练：风险目标与公平约束'),(979,'决策：独立抽选阈值，再比较分数')]:t.label(561,y,title,36)
t.label(561,451,'补充遗漏人群，核实标签；虚线记录标签未知',30)
t.label(664,633,'经验风险',30)
t.text(664,690,[run('min R', 'math',34),run('̂','math',34),run('tr','math',22,7),run('(f)','math',34)])
t.label(936,633,'公平约束',30)
t.text(936,690,[run('Δ̂','math',34),run('tr','math',22,7),run('(f) ≤ η','math',34)])
t.label(561,893,'调整训练目标和约束，不能替代其他环节的审计',30)
t.text(507,1029,[run('T','math',28),run('1','math',20,5)])
t.text(507,1145,[run('T','math',28),run('2','math',20,5)])
t.label(642,1035,'T',30,'math')
t.label(220,1232,'分数 S',30)
t.label(794,1227,'S ≥ T',34,'math')
t.text(1070,1229,[run('ŷ','math',30)])
t.label(561,1344,'各半概率抽选，与个人分数独立；再比较 S 和 T',28)
t.save()
check=json.loads((HERE/'typography-check.json').read_text());check.update(width_mm=132,minimum_primary_pt=28*132/25.4*72/t.base.width,label_pair_overlaps=[])
for a,b in itertools.combinations(t.labels,2):
 for aa in a['boxes']:
  for bb in b['boxes']:
   if min(aa[2],bb[2])>max(aa[0],bb[0]) and min(aa[3],bb[3])>max(aa[1],bb[1]):check['label_pair_overlaps'].append([aa,bb])
assert not check['label_pair_overlaps'],check
(HERE/'typography-check.json').write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n')
(HERE/'typesetting.json').write_text(json.dumps(dict(background='background-redraw-20261013.png',labels_source='labels.json',text_layer='text-layer.png',renderer=str(Path(__file__).relative_to(ROOT)),width_mm=132,generation_record='generation-redraw-20261013.json'),ensure_ascii=False,indent=2)+'\n')
report_path=ROOT/'figures/06-foundations/00-shared/generated/restoration-report.json';report=json.loads(report_path.read_text())
r=next(r for r in report['records'] if r['id']=='067');r.update(pixels=list(t.base.size),layout='New model artwork: three vertical stages; independent decision inputs',method='built-in image_gen.imagegen with real-font overlay',panel_transforms=None,model_redraw_20261013=True,body_width_mm=132,sha256=hashlib.sha256((HERE/'figure.png').read_bytes()).hexdigest(),refinement='Model redraw with real-font labels; three compact vertical stages and independent threshold selection.',refinement_renderer=str(Path(__file__).relative_to(ROOT)),check=check)
report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');(HERE/'restoration-20261013.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
