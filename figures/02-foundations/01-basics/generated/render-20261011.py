"""Actual-font overlay for approved 2026-10-11 backgrounds; no artwork edits."""
from pathlib import Path
import sys,json,hashlib,argparse
from PIL import Image
ROOT=next(p for p in Path(__file__).resolve().parents if (p/"build.sh").exists())
sys.path.insert(0,str(ROOT/"figures/02-foundations/00-shared/generated"))
from typeset_common import Typeset,run,mathvar
BASE=Path(__file__).resolve().parent
# Coordinates are authored from actual viewed model outputs, in native pixels.
CHOICES={"introduction-data-split":4,"models-discriminative-generative":2,
"supervised-learning":1,"unsupervised-topics":1,"reinforcement-loop":4,
"semi-supervised-learning":3,"masked-self-supervision":2,"contrastive-learning":3,
"active-learning":5,"continual-learning":1,"multi-task-learning":5,
"transfer-learning":1,"meta-learning":6,"online-feedback-order":4,"federated-learning":3}
LABELS={
"introduction-data-split":[
(125,256,"训练集"),(125,533,"验证集"),(125,759,"测试集"),
(517,178,"拟合预处理"),(517,315,"估计参数"),(915,262,"候选模型"),
(915,605,"选择并冻结"),(1304,523,"冻结后的模型"),(1613,737,"仅评价")],
"models-discriminative-generative":[
(248,186,"邮件特征 x"),(628,249,"Logistic得分"),(628,312,"s = ln 3"),
(1066,249,"条件类别概率"),(1066,312,"σ(s) = 0.75"),
(1510,188,"类别0"),(1510,234,"0.25"),(1510,337,"类别1"),(1510,382,"0.75"),
(242,538,"先验 p(y)"),(242,578,"0.8 / 0.2"),
(242,687,"类内事件概率"),(242,728,"0.01 / 0.12"),
(660,606,"联合概率"),(660,665,"0.008 / 0.024"),
(1066,606,"归一化"),(1066,665,"除以 0.032"),
(1510,533,"类别0"),(1510,574,"0.25"),(1510,685,"类别1"),(1510,727,"0.75")],
"supervised-learning":[
(284,246,"训练输入 x"),(284,386,"3",22,"math","#FFFFFF"),
(729,269,"模型 fθ"),(1138,279,"预测 ŷ"),(1138,372,"8",12,"math"),
(1485,79,"训练目标 y"),(1485,165,"3",12,"math"),
(1485,325,"损失 L"),(802,548,"冻结参数",7.5,"note"),
(284,604,"新输入 x"),(284,748,"8",22,"math","#FFFFFF"),(729,630,"固定模型 fθ"),
(1138,630,"预测 ŷ"),(1138,732,"8",12,"math")],
"unsupervised-topics":[
(333,244,"无标签文档"),(334,319,"球队 比赛"),(334,381,"银行 贷款"),(334,443,"服务器 网络"),
(788,298,"学习主题分布"),(1308,97,"主题1：体育"),(1308,141,"球队 比赛"),
(1308,272,"主题2：金融"),(1308,316,"银行 贷款"),(1308,446,"主题3：科技"),(1308,490,"服务器 网络"),
(861,546,"保留主题",7.5,"note"),(269,696,"新文档"),(269,763,"银行"),(269,817,"网络"),
(788,778,"推断主题比例"),(1310,639,"主题1：θ₁"),(1310,776,"主题2：θ₂"),(1310,912,"主题3：θ₃")],
"reinforcement-loop":[
(239,477,"观测与历史"),(689,477,"策略 πθ"),(1088,472,"动作 a"),
(1529,292,"环境"),(1088,181,"交互记录"),(690,181,"学习更新"),
(1088,758,"新观测与奖励"),(414,800,"非终止时继续",7.5,"note")],
"semi-supervised-learning":[
(398,111,"带标签样本"),(188,356,"狗"),(385,356,"猫"),(591,356,"鸟"),
(398,451,"无标签样本"),(932,247,"监督目标"),(910,682,"无标签目标"),
(1139,479,"分类器 fθ"),(1585,387,"新样本 x"),(1235,757,"预测：猫")],
"masked-self-supervision":[
(518,213,"原始文本"),(129,301,"猫"),(269,301,"在"),(418,301,"垫子"),(568,301,"上"),
(1042,62,"保留目标"),(1042,143,"垫子"),(482,490,"掩码输入"),
(292,583,"猫"),(418,583,"在"),(544,583,"[MASK]",7.5,"math"),(670,583,"上"),
(998,427,"模型 fθ"),(1363,491,"预测词元"),(1363,588,"垫子"),(1745,469,"掩码损失 L"),
(1400,798,"更新参数",7.5,"note")],
"contrastive-learning":[
(214,198,"原始样本"),(624,123,"视图1"),(624,338,"视图2"),(214,551,"不同样本"),
(1020,235,"共享编码器 fθ"),(1502,232,"表示空间"),
(1455,448,"拉近",7.5,"note"),(1655,485,"拉远",7.5,"note")],
"active-learning":[
(270,119,"带标签集合"),(888,95,"训练模型"),(1484,250,"未标注池：10"),
(884,589,"查询人工标签"),(287,516,"剩余候选：9"),
(285,438,"模型更新后再选",7.5,"note"),(287,852,"旧边界虚线；新边界实线",7.5,"note"),
(107,223,"0",8,"math","#FFFFFF"),(214,223,"1",8,"math","#FFFFFF"),
(321,223,"2",8,"math","#FFFFFF"),(429,223,"4",8,"math","#FFFFFF"),
(107,272,"0"),(214,272,"1"),(321,272,"2"),(429,272,"4"),
(1320,332,"0",8,"math","#FFFFFF"),(1604,332,"1",8,"math","#FFFFFF"),
(1277,401,"2",8,"math","#FFFFFF"),(1378,385,"4",8,"math","#FFFFFF"),
(1453,422,"3",8,"math","#FFFFFF"),(1680,389,"5",8,"math","#FFFFFF"),
(1335,460,"6",8,"math","#FFFFFF"),(1572,443,"7",8,"math","#FFFFFF"),
(1420,515,"8",8,"math","#FFFFFF"),(1634,523,"9",8,"math","#FFFFFF"),
(914,709,"3",12,"math","#FFFFFF"),(1026,714,"3",10,"math"),
(128,596,"0",8,"math","#FFFFFF"),(355,596,"1",8,"math","#FFFFFF"),
(488,621,"8",8,"math","#FFFFFF"),(186,654,"2",8,"math","#FFFFFF"),
(405,672,"4",8,"math","#FFFFFF"),(85,692,"5",8,"math","#FFFFFF"),
(240,729,"6",8,"math","#FFFFFF"),(439,741,"7",8,"math","#FFFFFF"),
(150,761,"9",8,"math","#FFFFFF")],
"continual-learning":[
(281,114,"阶段1：新增鸟、车"),(854,114,"阶段2：新增狗、船"),(1457,114,"阶段3：新增花、工具"),
(281,481,"模型 f₁"),(854,481,"模型 f₂"),(1457,481,"模型 f₃"),
(281,640,"评价2类"),(854,640,"评价4类"),(1457,640,"评价6类")],
"multi-task-learning":[
(196,336,"街景输入 x"),(510,437,"共享层 fθ"),(760,160,"分割头 g₁"),
(1063,160,"分割预测"),(1592,160,"分割目标"),(1328,273,"L₁"),
(760,558,"深度头 g₂"),(1063,558,"深度预测"),(1592,558,"深度目标"),(1328,670,"L₂")],
"transfer-learning":[
(251,98,"源任务样本"),(686,235,"源学习表示"),(993,285,"目标任务适应"),
(276,556,"少量目标标签"),(117,760,"玫瑰"),(276,760,"向日葵"),(434,760,"郁金香"),
(1301,294,"目标模型 fθ"),(1625,325,"目标预测"),(1625,402,"郁金香"),(1301,777,"新样本 x")],
"meta-learning":[
(768,111,"共同起点 θ"),(132,235,"任务1"),(488,235,"任务2"),(841,235,"任务3"),(1225,235,"新任务"),
(132,264,"支持集"),(488,264,"支持集"),(841,264,"支持集"),(1225,264,"支持集"),
(132,466,"检查集"),(488,466,"检查集"),(841,466,"检查集"),(1225,466,"检查集"),
(297,371,"适应 θ′₁"),(654,371,"适应 θ′₂"),(1011,371,"适应 θ′₃"),(1409,371,"任务适应"),
(283,699,"检查 L₁"),(639,699,"检查 L₂"),(996,699,"检查 L₃"),(1404,699,"只评价"),
(681,904,"跨任务更新")],
"online-feedback-order":[
(145,268,"输入 xₜ"),(412,268,"模型 fₜ"),(653,268,"预测 ŷₜ"),(936,268,"反馈 yₜ"),
(1160,268,"更新参数"),(1410,268,"模型 fₜ₊₁"),(1654,268,"预测 ŷₜ₊₁"),
(803,231,"延迟",7.5,"note"),(1410,429,"新输入 xₜ₊₁"),
(144,697,"输入 xₜ"),(413,697,"固定模型 f"),(658,697,"预测 ŷₜ"),
(1073,697,"新输入"),(1330,697,"固定模型 f"),(1630,697,"新预测"),
(137,164,"在线更新",7.5,"note"),(147,595,"流式使用",7.5,"note")],
"federated-learning":[
(162,478,"共享 θᵗ"),(609,105,"本地 D₁"),(609,356,"本地 D₂"),(609,607,"本地 D₃"),
(609,236,"本地训练"),(609,480,"本地训练"),(609,734,"本地训练"),
(920,236,"本地 θ₁"),(920,480,"本地 θ₂"),(920,734,"本地 θ₃"),
(1271,478,"按样本量聚合"),(1612,478,"下一轮 θ")]}
def typeset(slug):
 rev=CHOICES[slug]; bg=BASE/slug/f"background-20261011-r{rev}.png"
 width_mm=164.6
 t=Typeset(bg,BASE/slug,ROOT/"fonts")
 pt_per_px=width_mm/25.4*72/t.base.width
 for row in LABELS[slug]:
  x,y,text,*opt=row; pt=opt[0] if opt else 8; kind=opt[1] if len(opt)>1 else "cn"; color=opt[2] if len(opt)>2 else "#3B4252"
  if kind in ('cn','note'):
   seg=[]
   for ci,c in enumerate(text):
    sub={'₀':'0','₁':'1','₂':'2','₃':'3','ₜ':'t','₊':'+','ᵢ':'i'}
    if c in sub:
     seg.append(run(sub[c],'math',pt/pt_per_px*.65,pt/pt_per_px*.18));continue
    if c=='ᵗ':
     seg.append(run('(t)','math',pt/pt_per_px*.65,-pt/pt_per_px*.45));continue
    if c=='θ' and ci and text[ci-1] in ('f','π'):
     seg.append(run('𝜃','math',pt/pt_per_px*.65,pt/pt_per_px*.18));continue
    cp=ord(c)
    font='math' if (33<=cp<=126 or 0xC0<=cp<=0x24F or 0x300<=cp<=0x3ff or 0x2070<=cp<=0x22ff or 0x1d400<=cp<=0x1d7ff) else kind
    if seg and seg[-1]['font']==font and seg[-1]['size']==pt/pt_per_px and seg[-1]['dy']==0:seg[-1]['text']+=c
    else:seg.append(run(c,font,pt/pt_per_px))
   t.text(x,y,seg,color)
  else:t.label(x,y,text,size=pt/pt_per_px,kind=kind,color=color)
 t.save()
 meta=dict(background=bg.name,background_sha256=hashlib.sha256(bg.read_bytes()).hexdigest(),
  width_mm=width_mm,pixels=list(t.base.size),point_per_pixel=pt_per_px,main_pt=8,note_pt=7.5,
  selected_revision=rev,artwork_changes_by_overlay=False,code=str(Path(__file__).relative_to(ROOT)),
  labels="labels.json",layer="text-layer.png",status="typeset; actual visual review required")
 (BASE/slug/"typesetting-20261011.json").write_text(json.dumps(meta,ensure_ascii=False,indent=2)+"\n")
 print(slug,t.base.size,round(pt_per_px,5))
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("slugs",nargs="*");a=p.parse_args()
 for slug in a.slugs or CHOICES:typeset(slug)
