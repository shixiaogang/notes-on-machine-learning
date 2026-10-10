"""Exact teaching functions from the chapter, not empirical or generated curves."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt,font_manager as fm
from matplotlib.mathtext import MathTextParser
from fontTools.ttLib import TTFont

def make_panels(out,fonts):
    out=Path(out);fonts=Path(fonts)
    fira=fm.FontProperties(fname=str(fonts/'FiraMath-Regular.otf'))
    cn=fm.FontProperties(fname=str(fonts/'SourceHanSansSC-Normal.otf'))
    for f in ['FiraMath-Regular.otf','SourceHanSansSC-Normal.otf','LXGWWenKai-Regular.ttf']:fm.fontManager.addfont(str(fonts/f))
    matplotlib.rcParams.update({'font.family':fira.get_name(),'mathtext.fontset':'custom','mathtext.rm':fira.get_name(),'mathtext.it':fira.get_name(),'mathtext.bf':fira.get_name(),'mathtext.fallback':None,'pdf.fonttype':42,'svg.fonttype':'none','axes.unicode_minus':False})
    fira.set_math_fontfamily('custom')
    parser=MathTextParser('path');glyph_fonts=set()
    for expression in [r'$H(𝑧)$',r'$\psi(𝑧)=1/(1+|𝑧|)^2$',r'$𝑧=𝑣-\vartheta$']:
        parsed=parser.parse(expression,dpi=110,prop=fira)
        glyph_fonts.update(str(Path(g[0].fname).resolve()) for g in parsed.glyphs)
    assert glyph_fonts=={str((fonts/'FiraMath-Regular.otf').resolve())},glyph_fonts
    cn_cmap=TTFont(fonts/'SourceHanSansSC-Normal.otf').getBestCmap()
    assert all(ord(c) in cn_cmap for c in '前向：真实阶跃反向：指定替代规则')
    ink='#3B4252';blue='#7B95C6';rose='#C85E62'
    z=np.linspace(-2,2,4001);psi=1/(1+np.abs(z))**2
    np.savetxt(out/'analytic-function-data.csv',np.column_stack([z,(z>=0).astype(float),psi]),delimiter=',',header='z,H(z),psi(z)',comments='')
    results=[]
    for kind,title,color in [('step','前向：真实阶跃',blue),('psi','反向：指定替代规则',rose)]:
        fig,ax=plt.subplots(figsize=(390/110,290/110),dpi=110)
        fig.subplots_adjust(left=.16,right=.96,bottom=.23,top=.82)
        if kind=='step':
            ax.plot([-2,0],[0,0],color=color,lw=2.1)
            ax.plot([0,2],[1,1],color=color,lw=2.1)
            ax.plot(0,0,'o',ms=5,mfc='white',mec=color,mew=1.5,zorder=4)
            ax.plot(0,1,'o',ms=5,mfc=color,mec=color,zorder=4)
            ax.text(.98,.78,r'$H(𝑧)$',ha='right',va='top',transform=ax.transAxes,color=ink,fontsize=13,fontproperties=fira)
        else:
            ax.plot(z,psi,color=color,lw=2.1)
            ax.text(.99,.97,r'$\psi(𝑧)=1/(1+|𝑧|)^2$',ha='right',va='top',transform=ax.transAxes,color=ink,fontsize=10.7,fontproperties=fira)
        ax.axvline(0,color='#6B7280',lw=.8,ls=(0,(3,3)),zorder=0)
        ax.set_xlim(-2,2);ax.set_ylim(-.1,1.18)
        ax.set_xticks([-2,0,2]);ax.set_yticks([0,1])
        ax.set_title(title,fontproperties=cn,fontsize=14,color=ink,pad=10)
        ax.set_xlabel(r'$𝑧=𝑣-\vartheta$',fontproperties=fira,fontsize=13,color=ink)
        for edge in ['top','right']:ax.spines[edge].set_visible(False)
        for edge in ['left','bottom']:ax.spines[edge].set_color('#6B7280');ax.spines[edge].set_linewidth(.8)
        ax.tick_params(labelsize=12,colors=ink,width=.7,length=3)
        for tick in ax.get_xticklabels()+ax.get_yticklabels():tick.set_fontproperties(fira);tick.set_fontsize(12)
        p=out/f'analytic-{kind}.png'
        fig.savefig(p,dpi=110,facecolor='white');fig.savefig(out/f'analytic-{kind}.pdf',facecolor='white');fig.savefig(out/f'analytic-{kind}.svg',facecolor='white')
        plt.close(fig);results.append(p)
    record=dict(source='Textbook equations snn-discrete-fire and snn-surrogate-derivative',type='analytic teaching example, no empirical observations',formula_H='H(z)=0 for z<0 and H(z)=1 for z>=0',formula_psi='c/(1+kappa*abs(z))^2',parameters=dict(c=1,kappa=1),domain=[-2,2],samples=4001,plot_discontinuity='Separate constant branches; open point at (0,0), closed point at (0,1), no interpolated jump segment.',font_cn=str(fonts/'SourceHanSansSC-Normal.otf'),font_en_math=str(fonts/'FiraMath-Regular.otf'),font_fallback=False,mathtext_glyph_font_files=sorted(glyph_fonts),missing_glyphs=0,panel_pixels=[390,290])
    (out/'analytic-functions.json').write_text(json.dumps(record,ensure_ascii=False,indent=2))
    assert psi[2000]==1 and np.isclose(psi[0],1/9) and z[2000]==0
    return results

if __name__=='__main__':
    root=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
    make_panels(Path(__file__).parent,root/'fonts')
