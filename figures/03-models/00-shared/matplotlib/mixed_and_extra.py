"""Three per-panel mixed previews; two quantitative event/scaling charts.

Quantitative values are analytic, exactly retained teaching inputs. Topology is
drawn with TikZ, not a model, while sampled values use Matplotlib. No body edits.
"""
from pathlib import Path
import sys,json,shutil,importlib.util
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import fitz
from numeric_relations import ROOT,fig,axes,C,N
from plot_style import configure,prepare_figure,note,BLUE,GREEN,RED,MUTED,INK,GRID,BLUE_FILL,GREEN as MODEL,RED_FILL
from export_common import save
from production_paths import ITEMS,destination
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'));from render_tikz import render

def panel_export(f,key):
 save(f,Path(next(x['sources'][0] for x in ITEMS if x['key']==key)).stem,data=DATA,params=PARAMS,inputs=INPUTS)
 dest=destination(key)
 for ext in ['pdf','svg','png']:shutil.move(dest/('figure.'+ext),dest/('chart.'+ext))
 shutil.move(dest/'generation.json',dest/'chart-generation.json')

def compose(key,width,height,rects):
 dest=destination(key);doc=fitz.open();page=doc.new_page(width=width*72/25.4,height=height*72/25.4)
 for filename,coords in rects:
  with fitz.open(dest/filename) as d:page.show_pdf_page(fitz.Rect([c*72/25.4 for c in coords]),d,0,keep_proportion=True)
 doc.save(dest/'figure.pdf');page.get_pixmap(dpi=300).save(dest/'figure.png');(dest/'figure.svg').write_text(page.get_svg_image(text_as_path=True));doc.close()
 (dest/'generation.json').write_text(json.dumps({'key':key,'route':'TikZ relation panel + Matplotlib quantitative panel','source':'figures/03-models/00-shared/matplotlib/mixed_and_extra.py','panels':[{'file':x,'rectangle_mm':r} for x,r in rects],'physical_size_mm':[width,height],'numeric_source':'chart-generation.json','topology_source':'topology.tex','exports':['PDF vector','SVG paths','PNG300dpi'],'body_edits':False,'status':'Rendered; visual review required'},ensure_ascii=False,indent=2)+'\n')

configure()
f,a=fig(112,56);axes(a,(.4,8.7),(-.2,1.4),'时间区间 $t$','',[1,2,3,4,5,6,7,8],[])
for y,events,c,label in [(1,[1,2,6],BLUE,'脉冲列 A'),(0,[3,5,8],GREEN,'脉冲列 B')]:
 a.hlines(y,.4,8.5,color=MUTED,lw=.6);a.vlines(events,y,y+.33,color=c,lw=1.5);note(a.text(.35,y+.12,label,ha='right',va='center'))
a.spines['left'].set_visible(False);a.spines['bottom'].set_visible(False)
save(f,'snn-codes',data={'A_events':[1,2,6],'B_events':[3,5,8]},params={'time_axis':[1,8],'pulse_height':'schematic, no amplitude claim'},inputs=[N/'snn-codes.tex'])

f,aa=fig(169,69,ncols=2)
for a,title,labels in [(aa[0],'HBM 中间量',[r'$\Theta(n^2)$',r'$\Theta(nd)$']),(aa[1],'访存主项',[r'$\Theta(n^2)$',r'$\Theta(n^2d^2/M)$'])]:
 bars=a.bar([0,1],[46,15],width=.55,color=[BLUE_FILL,RED_FILL],edgecolor=[BLUE,RED],linewidth=.8)
 a.set(xticks=[0,1],xticklabels=['常规注意力','FlashAttention'],yticks=[],ylim=(0,62),title=title)
 a.set_ylabel('示意量（非实测比例）')
 for x,h,t in zip([0,1],[46,15],labels):a.text(x,h+3,t,ha='center',va='bottom')
save(f,'transformer-flashattention-io',data={'schematic_bar_heights':[46,15],'numeric_ratio_claimed':False},params={'purpose':'Compare symbolic resident/intermediate and I/O scaling; heights retained only as schematic geometry.','resident_tensor':'Theta(nd)','IO':'Theta(n^2*d^2/M)','not_measured':True},inputs=[N/'transformer-flashattention-io.tex'])

key='regression-tree-prediction';dest=destination(key)
s=(C/(key+'.tex')).read_text();s=s[:s.index('  \\fill[FigureInput] (83,56)')]+r'\end{tikzpicture}'+'\n'
s=s.replace('(158,64)','(75,64)').replace('  \\node[anchor=west,inner sep=0pt] at (82,61) {(b) 一维分段常数预测};','').replace('  \\draw[FigureGrid,line width=0.5pt] (75,6)--(75,58);','').replace(r'\bfseries',r'\mdseries').replace('text=FigureOutput,','text=FigureInk,')
s=s.replace('node[pos=0.5,left,inner sep=1pt]','node[pos=0.5,left,inner sep=1pt,font=\\FigureNoteFont\\footnotesize]').replace('node[pos=0.5,right,inner sep=1pt]','node[pos=0.5,right,inner sep=1pt,font=\\FigureNoteFont\\footnotesize]')
(dest/'topology.tex').write_text(s);render(dest/'topology.tex',dest)
f,a=fig(84,67);axes(a,(0,6),(0,5.6),'$x$（无量纲）','$y, f_T(x)$（无量纲）',[.5,1.5,2.5,3.5,4.5,5.5],[0,1,2,3,4,5],True)
x=np.arange(.5,6,.9999999999999999);x=np.array([.5,1.5,2.5,3.5,4.5,5.5]);y=np.array([1,2,4,5,2,3])
a.scatter(x,y,c=BLUE,s=16,label='观测样本')
for lo,hi,val,i in [(0,2,1.5,1),(2,4,4.5,2),(4,6,2.5,3)]:
 a.plot([lo,hi],[val,val],c=RED,ls='--',label='$f_T(x)$' if i==1 else None)
 note(a.text((lo+hi)/2,{1:.45,2:3.25,3:1.2}[i],r'$R_'+str(i)+r':c_'+str(i)+'='+str(val)+'$',ha='center'))
for boundary,left,right in [(2,1.5,4.5),(4,4.5,2.5)]:
 a.axvline(boundary,c=GREEN,lw=.6);a.scatter([boundary],[left],c=RED,s=17,zorder=4);a.scatter([boundary],[right],fc='white',ec=RED,s=17,zorder=4)
a.legend(loc='upper right',fontsize=7);a.set_title('(b) 分段常数预测',loc='left')
DATA={'x':x,'y':y,'thresholds':[2,4],'leaf_means':[1.5,4.5,2.5]};PARAMS={'threshold_equality':'belongs to left interval; upper open/lower closed as shown','supplied_fixed_tree':True,'unweighted_squared_loss':True};INPUTS=[C/(key+'.tex')];panel_export(f,key)
compose(key,169,72,[('topology.pdf',[0,1,77,71]),('chart.pdf',[82,0,169,72])])

key='pgm-sampling-hmc';dest=destination(key)
s=r'''\begin{tikzpicture}[x=1mm,y=1mm,font=\figurefont\footnotesize,
 flow/.style={draw=FigureStroke,align=center,text width=42mm,minimum height=13mm,inner sep=2mm}]
 \node[flow,fill=FigureInputFill] (refresh) at (25,54) {动量刷新\\$\bm{r}\sim\mathcal{N}(\bm{0},\bm{M})$};
 \node[flow,fill=FigureModelFill] (integrate) at (25,29) {蛙跳积分与动量翻转\\$T=R\Phi_\epsilon^L$};
 \node[flow,fill=FigureOutputFill] (correct) at (25,4) {末端Metropolis校正\\拒绝时保留原位置};
 \draw[-{Stealth[length=1.8mm]},FigureStroke] (refresh)--(integrate);
 \draw[-{Stealth[length=1.8mm]},FigureStroke] (integrate)--(correct);
\end{tikzpicture}
''';(dest/'topology.tex').write_text(s);render(dest/'topology.tex',dest)
t=np.linspace(0,np.pi/2,41);f,a=fig(84,84);axes(a,(-.05,1.35),(-.05,1.4),'$z$','$r$',[0,.5,1],[0,.5,1]);a.set_aspect('equal');a.plot(np.sin(t),np.cos(t),c=MUTED,ls='--');a.annotate('',(.5,1),(0,1),arrowprops={'arrowstyle':'->','color':BLUE});a.annotate('',(.5,.875),(.5,1),arrowprops={'arrowstyle':'->','color':RED});a.scatter([0],[1],c=BLUE,s=22);a.scatter([.5],[.875],c=GREEN,s=22,zorder=4);note(a.text(.25,1.08,'位置整步',ha='center'));note(a.text(.74,1.13,"$z'=0.5$\n$r'=0.875$",va='top'));note(a.text(.5,-.40,r'$H:0.5\to0.5078125$'+'\n接受率 $\\approx0.992218$',transform=a.transAxes,ha='center'));a.set_title('相空间中的一步蛙跳')
DATA={'trajectory':[[0,1],[.5,1],[.5,.875]],'exact_energy':[.5,.5078125],'acceptance':float(np.exp(-.0078125)),'exact_orbit_z':np.sin(t),'exact_orbit_r':np.cos(t)};PARAMS={'target':'standard normal','M':1,'epsilon':.5,'initial':[0,1],'orbit_samples':41};INPUTS=[ROOT/'figures/03-models/03-probabilistic-graphical-models/tikz/pgm-sampling-hmc.tex'];panel_export(f,key)
compose(key,151,88,[('chart.pdf',[0,0,88,88]),('topology.pdf',[95,0,151,88])])

key='dim-diffusion-walk';dest=destination(key)
s=(C/(key+'.tex')).read_text();s=s[:s.index('  \\node[anchor=east] at (29,77)')]+r'\end{tikzpicture}'+'\n';s=s.replace('(0,0) rectangle (112,125)','(20,87) rectangle (112,125)');(dest/'topology.tex').write_text(s);render(dest/'topology.tex',dest)
spec=importlib.util.spec_from_file_location('exact_diffusion',C/'dim-diffusion-walk.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);snapshots,stationary=module.compute()
arrays={str(t):np.array([[float(module.decimal(snapshots[t][row][j])) for j in range(6)] for row in [0,5]]) for t in [1,4,64]}
f=plt.figure(figsize=(112/25.4,87/25.4),layout='constrained');gs=f.add_gridspec(4,1,height_ratios=[1,1,1,.15]);cmap=LinearSegmentedColormap.from_list('lancet_blue',['white',BLUE]);labels=['左1','左2','左3','右1','右2','右3']
for i,t in enumerate([1,4,64]):
 a=f.add_subplot(gs[i]);v=arrays[str(t)];im=a.pcolormesh(np.arange(7)-.5,np.arange(3)-.5,v,cmap=cmap,vmin=0,vmax=1/3,shading='flat');a.set_ylim(1.5,-.5);a.set_yticks([0,1],['左1出发','右3出发']);a.set_xticks(range(6),labels if i==0 else []);a.xaxis.tick_top();a.tick_params(length=0);a.set_title('$t='+str(t)+'$',loc='left');a.axvline(2.5,c=MUTED,ls='--',lw=.6)
 for row in range(2):
  for col in range(6):a.text(col,row,f'{v[row,col]:.3f}',ha='center',va='center',color='white' if v[row,col]>.22 else INK)
cbar=f.colorbar(im,cax=f.add_subplot(gs[3]),orientation='horizontal',ticks=[0,1/6,1/3]);cbar.set_label('概率（所有面板共用色标）',labelpad=2)
cbar.solids.set_rasterized(False) # Preserve the quantitative color bar as vector cells.
DATA=arrays;PARAMS={'alpha':0,'kernel_within_group':1,'bridge_weight':.15,'row_stochastic':True,'stationary':[float(q) for q in stationary],'color_range':[0,1/3],'matrix_power_times':[1,4,64],'exact_data_source':'dim-diffusion-walk.py Fraction matrix powers','displayed_original_six_decimal_values_retained':True};INPUTS=[C/'dim-diffusion-walk.py',C/(key+'.tex')];panel_export(f,key)
compose(key,112,129,[('topology.pdf',[0,0,112,40]),('chart.pdf',[0,42,112,129])])
