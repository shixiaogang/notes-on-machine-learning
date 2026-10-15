# -*- coding: utf-8 -*-
from pathlib import Path
import json, hashlib

root = Path(__file__).resolve().parents[4]
review = root / 'reviews/volume-one-readable-review-2026-10-12'
dest = Path(__file__).resolve().parent
source = root / 'tex/02-mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/04-multi-agent-response-and-evolution.tex'
text = source.read_text()
original = {x['id']: x for f in (review/'initial/ch16').glob('*/findings.json') for x in json.loads(f.read_text())}
items = [
(['CH16-A-01','CH16-B-02','CH16-C-01','CH16-C-02'], '局部费力', '有据撤销', r'\scite{math-zinkevich2003online}设', '逐处核对五个引用后位置；scite无条件输出中文句号，源码中已有句号被吸收。', '五处引文所在段到下一定义、定理或主句', 'tex/styles/references.tex中的scite无条件输出nobreak中文句号；源码没有字面句号不等于PDF缺少句界。'),
(['CH16-B-01'], '理解障碍', '修改', r'T_{\mathrm{loc}}', '时域改Tloc，历史集合改花体H和H_i，跨轮可用信息改script I，保留H作为牌面或硬币标签。', '时域式、历史树与信息集、跨轮更新式', '时域、历史集合与牌面在各自局部的类型不再碰撞；牌面及图源记号保持一致。'),
(['CH16-A-02'], '局部费力', '修改', '这里的信念是参与者', '首现处解释信息集内历史的条件分布、零概率Bayes分母和逐信息集最优的序贯理性。', '完整策略偏离至行为策略入口', '必要白话在首次使用处给出，不能由后文CFR后验例倒补；额外相容条件仍明示。'),
(['CH16-A-03'], '技术问题', '修改', '固定对手策略后，本人的收益', '给连续收益的argmax非空且闭于紧单纯形，因而各值集紧的论证。', '上半连续定义、闭图判据与等价证明', '域紧和值集紧有不同依据，未由所有值位于紧域推出任意值集紧。'),
(['CH16-B-03'], '理解障碍', '修改', '这是另一项分配选择任务', '入口分清联盟稳定与协商选择，转换和结尾分别写明Nash乘积不证核心或动态稳定。', '合作分配下的偏离与稳定整小节', '标题保留，正文分工明确；收益选择公理不被冒称联盟无阻挡。'),
(['CH16-A-04'], '局部费力', '修改', '占比为正的类型', '展开正比例为占比为正，并把缺席对象明确定为初始零占比类型。', '复制方程到纯顶点解释与双群体例', '零坐标在无变异方程下不变；代词不再误指当前驻留类型。'),
(['CH16-B-04'], '局部费力', '修改', r'记$F(p,q)=p(1-p)q(1-q)$', '补严格凹logF和径向单调性、紧光滑闭曲线、非零切向速度及周期返回桥。', '双群体复制方程至ESS入口', '0<c<1/16的水平集避边界且梯度不为零，紧曲线上速度有正下界，有限绕行与解唯一性支持周期性。'),
(['CH16-B-05'], '理解障碍', '修改', '实现计划记录的是本人', '首现处说明自身序列权重，正式权重定义后将相容坐标与空序列1命名为实现计划。', '平均入口、两层小树、实现权重及前驱流量归纳', '对象是本人相容到达权重；不是全路径律，也不是任意局部行为概率算术平均。'),
]
rows = []
for number, (ids, severity, decision, quote, action, context, reason) in enumerate(items, 1):
    assert quote in text, quote
    rows.append(dict(merged_id=f'CH16-M-{number:02}', original_ids=ids, severity=severity, decision=decision,
        status='有据撤销' if decision=='有据撤销' else '已修改待独立复核',
        location_before=[dict(id=x, lines=original[x]['lines'], quote=original[x]['quote']) for x in ids],
        location_after=dict(source=str(source.relative_to(root)), line=text[:text.index(quote)].count('\n')+1, quote=quote),
        action=action, reread_range=context, closure_reason=reason, reviewer='主代理 AI 自查'))
rows.append(dict(merged_id='CH16-N-01', original_ids=[], severity='局部费力', decision='修改', status='已修改待独立复核',
    location_before=dict(quote='第 BookTheoremRef 号定理给出原对偶最优值相等'),
    location_after=dict(quote='有限维线性规划的原问题可行且最优值有限时，强对偶保证对偶也有最优解'),
    action='删除跨卷宏两侧的第和号定理；就地给强对偶关系、条件及本例用途，然后用可参考引用。',
    reread_range='零和LP两式及最优有限性说明至教学原对偶证书',
    closure_reason='跨卷宏显示卷和位置，不显示当前卷定理号；改后引用没有替代必要的强对偶说明。'))
(dest/'consolidated-findings.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')
(dest/'after.tex').write_bytes(source.read_bytes())
(dest/'snapshot-manifest.json').write_text(json.dumps(dict(source=str(source.relative_to(root)), date='2026-10-13',
    before_sha256=hashlib.sha256((dest/'before.tex').read_bytes()).hexdigest(), after_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
    original_findings=11, merged_findings=8, modified=7, revoked=1, additional_changes=1,
    status='正文局部修订复读完成，完整三级记录待补，待独立复核'), ensure_ascii=False, indent=2)+'\n')
print('11 original findings mapped to 8 merged units; 1 additional repair.')
