from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
SRC=Path('tex/01-mathematical-preliminaries-upper/03-graphs-and-signals/01-signal-representation-and-processing.tex')
BASE=Path(__file__).parent
p=SRC
if not (BASE/'before.tex').exists(): (BASE/'before.tex').write_text(p.read_text())
def change(num,ids,severity,old,new,reason,reread):
    text=p.read_text(); assert text.count(old)==1,(num,text.count(old))
    before=(BASE/'before.tex').read_text()
    line=before[:before.index(old)].count('\n')+1
    text=text.replace(old,new); p.write_text(text)
    f=BASE/'consolidated-findings.json'; data=json.loads(f.read_text()) if f.exists() else []
    data.append(dict(merged_id=f'CH08-M-{num:02d}',original_ids=ids.split(),severity=severity,decision='修改',location_before=dict(lines=f'L{line}-L{line+old.count(chr(10))}',quote=old),location_after=dict(lines='待最终定位',quote=new),action=reason,reread_range=reread,closure_reason='已按所列连续上下文复读：'+reason))
    f.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    with (BASE/'repair-notes.md').open('a') as out: out.write(f'\n- CH08-M-{num:02d}：{reason} 连续复读：{reread}。\n')
change(1,'CH08-A-01','局部费力','读数；若要查出持续振荡的快慢，可以把记录分解成不同频率的波动。两种表示\n描述同一条信号，但后续的滤波和采样会改变信号或可用的观测。','读数；若要查出持续振荡的快慢，可以把记录分解成不同频率的波动。前一种分析\n直接使用各时刻的读数，后一种分析改用频率系数描述同一条信号；\n后续的滤波和采样则会改变信号或可用的观测。','分别指出时刻读数和频率系数，不再把相邻读数比较直接称为表示。','章首四问至贯穿例')
change(2,'CH08-B-02','局部费力','对确定的卷积映射，我们还会比较五种计算路线，检查乘法数量减少后增加了哪些','对确定的卷积映射，我们以直接求和为基线，比较五种计算路线，检查乘法数量减少后增加了哪些','明确直接求和是基线，五个方法小节与含基线的六行表不再计数混淆。','章首计算承诺、快速计算节入口及算法比较表')
change(3,'CH08-C-01','理解障碍',r'''反射有不同端点约定。例如不重复端点且$N\geq2$时，
$x[-1]=x[1]$、$x[N]=x[N-2]$，再以$2(N-1)$为周期延续；
若重复端点，就有$x[-1]=x[0]$、$x[N]=x[N-1]$，得到另一个延拓。
两种方式都可能合理，但不是同一个输入。''',r'''反射有不同端点约定。先沿数组走到右端，再折返到左端，就能写出一个完整周期。
不重复端点且$N\geq2$时，把
$(x[0],\ldots,x[N-1],x[N-2],\ldots,x[1])$
按周期$2(N-1)$延续，$N=2$时其中的折返段为空。
重复端点时，把$(x[0],\ldots,x[N-1],x[N-1],\ldots,x[0])$
按周期$2N$延续。任意整数索引都先对相应周期取模，再读取该周期中的值。
例如记录$(1,2,1)$在$k=-2$处，两种反射分别得到$1$和$2$；
在$k=-1$处则分别得到$2$和$1$。若$N=1$，约定反射延拓恒等于唯一读数。
两种方式都可能合理，但不是同一个输入。''','用完整周期给出任意整数索引的反射规则，并核对跨两格及N=1、2边界。','有限支撑与边界延拓全小节')
change(4,'CH08-C-02','技术问题','各位置脉冲构成有限坐标空间的标准正交基，展开系数就是原读数，因此完整展开\n可逆。','先固定长度$N$的记录：限制在这$N$个位置上的脉冲构成$N$维坐标空间的标准正交基，\n展开系数就是原读数，因此完整展开可逆。','限定有限基对应固定N个位置；整轴有限支撑只限制单条信号而不限制整个空间维数。','时域表示全小节')
change(5,'CH08-A-02','技术问题','其余频率成对出现，使用单边频谱时必须说明这两个端点是否加倍。','其余频率成对出现。偶数$N$的单边频谱有直流与Nyquist两个自配对端点，\n奇数$N$则只有直流点自配对；合并共轭频率对时，须把这些自配对点与普通频率对分开处理。','显式区分奇偶长度的自配对频率，单边合并不再暗示所有N有两个端点。','共轭对称公式至八点余弦例及图注')
