from pathlib import Path
import sys, json, hashlib
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT/'figures/03-foundations/00-shared/generated'))
from typeset_common import Typeset

t = Typeset(HERE/'background-20261013.png', HERE, ROOT/'fonts')
for x, title, detail in [(265, '训练样本', '核实历史邮件标签'),
                         (806, '学习规则与训练', '形成训练模型'),
                         (1344, '预测与评价', '用评价样本检验预测')]:
    t.label(x, 773, title, 44)
    t.label(x, 846, detail, 40)
t.save()
check = json.loads((HERE/'typography-check.json').read_text())
check.update(width_mm=112, minimum_primary_pt=40*112/25.4*72/t.base.width)
(HERE/'typography-check.json').write_text(json.dumps(check, ensure_ascii=False, indent=2)+'\n')
(HERE/'typesetting.json').write_text(json.dumps(dict(background='background-20261013.png',
    renderer=str(Path(__file__).resolve().relative_to(ROOT)), labels_source='labels.json',
    text_layer='text-layer.png', body_width_mm=112), ensure_ascii=False, indent=2)+'\n')
