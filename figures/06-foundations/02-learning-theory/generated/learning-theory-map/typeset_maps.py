# Historical candidate source. For current publication output, use the canonical replay_labels.py command in generation.json.
"""Add actual fonts only; preserve the original model PNG geometry and colors."""
from pathlib import Path
import math, json, shutil
from PIL import Image, ImageDraw
from typeset_common import Typeset, run, INK, SCALE

BASE=Path(__file__).resolve().parent
FONT_CANDIDATES=[BASE/'fonts',BASE.parent/'fonts',BASE.parent.parent/'fonts']
FONTS=next(p for p in FONT_CANDIDATES if (p/'SourceHanSansSC-Normal.otf').exists())
CX,CY=626,616
COLORS=['#476D99']*3+['#4D826C']*3+['#A57444']*2
ANGLES=[293.4,338.4,20.0,65.0,112.5,157.5,202.5,247.5]
# Measured centers of the model's individual third-tier cells, clockwise.
# These are a topic hierarchy, not quantitative angle encodings.
LEAF_ANGLES={0:[276.05,288.2,305.55],1:[323.65,336.95,351.7],3:[52.9,72.5,84.05],4:[95.55,112.85,131.2],6:[188.25,203.05,217.3]}
LEAF_LINES={
 'learning-theory-map':{
  0:[['观测机制'],['归纳偏置'],['反馈与','可识别']],
  1:[['标签结构'],['恰当与','非恰当'],['损失与','解码']],
  3:[['随机','复杂度'],['压缩与','信息'],['有效样本','单位']],
  4:[['预训练','表示'],['上下文','学习'],['长度与','序列']],
  6:[['缩放定律'],['阈值与','涌现'],['顿悟与','推理计算']]},
 'trustworthiness-map':{
  0:[['危害情景'],['可检验','主张'],['处置阈值']],
  1:[['校准与','覆盖'],['拒答与','转交'],['主张级','核验']],
  3:[['复合偏移'],['变化监测'],['适应与','恢复']],
  4:[['归因与','反事实'],['机制解释'],['补救','有效性']],
  6:[['数据影响','与撤回'],['自适应','攻击'],['最小权限']]}}

CONFIG={
 'learning-theory-map':dict(
   title='机器学习理论', hub=['有限经验如何支持','可计算、可推广的','学习？'],
   themes=['问题与信息','泛化机制','实现与扩展'],
   branches=[['目标','可识别性'],['输出、标签','与损失结构'],['分布变化','与适应'],['样本与','复杂度'],['表示与','预训练'],['算法选解'],['规模与','能力变化'],['计算、资源','与验证']],
   leaves={0:['观测机制','归纳偏置','反馈与可识别'],1:['标签结构','恰当与非恰当','损失与解码'],3:['随机复杂度','压缩与信息','有效样本单位'],4:['预训练表示','上下文学习','长度与序列'],6:['缩放定律','阈值与涌现','顿悟与推理计算']}),
 'trustworthiness-map':dict(
   title='可信机器学习', hub=['真实使用中的系统','何时可以被依赖？'],
   themes=['要求与影响','证据与行为','防护与治理'],
   branches=[['要求','可操作化'],['未知识别','与转交'],['风险、收益','与负担分配'],['变化、适应','与恢复'],['解释、审计','与补救'],['目标、监督','与权限'],['隐私、安全','与行动保护'],['联合保证','与持续验证']],
   leaves={0:['危害情景','可检验主张','处置阈值'],1:['校准与覆盖','拒答与转交','主张级核验'],3:['复合偏移','变化监测','适应与恢复'],4:['归因与反事实','机制解释','补救有效性'],6:['数据影响与撤回','自适应攻击','最小权限']})}

def rotated_lines(t,x,y,lines,size,kind,color,screen_angle=0,spacing=None,role=None,parent=None,leaf=None):
 """True glyphs on a separate transparent text tile; rotate that tile, never artwork."""
 spacing=spacing or size*1.30
 f=t.font(kind,size)
 side=1000
 tile=Image.new('RGBA',(side,side),(0,0,0,0));d=ImageDraw.Draw(tile)
 centers=[]
 for i,line in enumerate(lines):
  by=side/2+(i-(len(lines)-1)/2)*spacing*SCALE
  box=d.textbbox((side/2,by),line,font=f,anchor='mm')
  d.text((side/2,by),line,font=f,fill=color,anchor='mm')
  centers.append(box)
 box=tile.getbbox();tile=tile.crop(box)
 tile=tile.rotate(-screen_angle,resample=Image.Resampling.BICUBIC,expand=True)
 px=round(x*SCALE-tile.width/2);py=round(y*SCALE-tile.height/2)
 t.layer.alpha_composite(tile,(px,py))
 bb=tile.getbbox()
 bbox=[round((px+bb[0])/SCALE,2),round((py+bb[1])/SCALE,2),round((px+bb[2])/SCALE,2),round((py+bb[3])/SCALE,2)]
 t.labels.append(dict(center_x=x,center_y=y,baseline_y=y,rotation_clockwise=screen_angle,segments=[run(line,kind,size) for line in lines],color=color,boxes=[bbox],role=role,parent_index=parent,leaf_index=leaf))

def point(radius,theta):
 a=math.radians(theta);return CX+radius*math.cos(a),CY+radius*math.sin(a)

def angle_readable(theta):
 a=(theta+90)%180
 return a if a<=90 else a-180

def produce(key,c):
 out=BASE if (BASE/'background.png').exists() else BASE/key
 t=Typeset(out/'background.png',out,FONTS)
 # Measured on each actual candidate: all three titles clear the semantic icons.
 t.label(835,556,c['themes'][0],24,'cn','#476D99')
 # 60 px left shift; the model icon was moved farther left first.
 t.label(680,842,c['themes'][1],24,'cn','#4D826C')
 t.label(414,561,c['themes'][2],24,'cn','#A57444')
 t.label(CX,580,c['title'],27,'cn',INK)
 note_y=[620,653,686] if len(c['hub'])==3 else [627,666]
 for line,y in zip(c['hub'],note_y):t.label(CX,y,line,22,'note',INK)
 for i,(theta,lines,color) in enumerate(zip(ANGLES,c['branches'],COLORS)):
  x,y=point(365,theta)
  rotated_lines(t,x,y,lines,25,'cn',color,angle_readable(theta),role='branch',parent=i)
 for i,questions in c['leaves'].items():
  for j,(question,lines,theta) in enumerate(zip(questions,LEAF_LINES[key][i],LEAF_ANGLES[i])):
   assert ''.join(lines)==question
   x,y=point(470,theta)
   rotated_lines(t,x,y,lines,19,'note',COLORS[i],angle_readable(theta),spacing=23,role='leaf',parent=i,leaf=j)
 t.save()
 if Path(__file__).resolve()!=(out/'typeset_maps.py').resolve():
  shutil.copy2(Path(__file__),out/'typeset_maps.py')
 if (BASE/'typeset_common.py').resolve()!=(out/'typeset_common.py').resolve():
  shutil.copy2(BASE/'typeset_common.py',out/'typeset_common.py')
 (out/'content.json').write_text(json.dumps(c,ensure_ascii=False,indent=2))

if __name__=='__main__':
 keys=[BASE.name if BASE.name in CONFIG else BASE.parent.name] if (BASE/'background.png').exists() else list(CONFIG)
 for key in keys:produce(key,CONFIG[key])
