"""Keep historical artwork and color ordering; re-typeset editable labels.

The user requested a volume-wide check on 2026-10-13 after identifying collapsed
color levels and poorly aligned text. Original backgrounds and labels are the
immutable inputs. The historical diagrams are retained; frame clearance is adjusted for 067.
"""
from pathlib import Path
import json, hashlib, importlib.util, itertools, math
import numpy as np
from PIL import Image, ImageDraw
from typeset_common import Typeset, FONT_FILES, SCALE, run

ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
HERE = Path(__file__).resolve().parent
FONT_FILES['fallback'] = 'STIXTwoMath-Regular.otf'
spec = importlib.util.spec_from_file_location('restore', HERE/'restore-pre-71bc2f9.py')
restore = importlib.util.module_from_spec(spec); spec.loader.exec_module(restore)
INK = '#3B4252'

# Only mechanism glyphs, never photographs, text bands or quantitative fields.
# These bounds were checked against the historical artwork and figure 13.4.
PRIMARY_REGIONS = {
 '010': [(327,310,605,515),(1230,353,1492,539),(760,655,850,746)],
 '013': [(1020,284,1345,516)],
 '018': [(220,375,375,480),(870,375,1025,480),(1510,375,1680,480)],
 '020': [(532,145,842,315),(532,584,806,752),(866,410,1000,571),
         (1050,410,1175,579),(1260,410,1425,590)],
 '042': [(122,306,480,640),(941,336,1323,659),(1500,424,1680,559),
         (750,435,833,495),(1708,461,1775,523),(176,678,453,793)],
 '076': [(487,150,730,267),(1003,150,1267,267),
         (487,347,730,460),(1003,347,1267,460),
         (487,539,730,652),(1003,539,1267,652)],
}

def emphasize_primary(original, current, number):
    """Anchor isolated solid glyph interiors to the canonical main colors.

    Preserve historical edges and antialiasing, large pale containers, and
    continuous scientific color fields. No object is added or moved.
    """
    from collections import deque
    src=np.array(original.convert('RGBA'));out=np.array(current.convert('RGBA'))
    changes=[]
    for x0,y0,x1,y1 in PRIMARY_REGIONS.get(number,[]):
        a=src[y0:y1,x0:x1,:3].astype(float)/255
        hi=a.max(2);lo=a.min(2);light=(hi+lo)/2
        sat=np.divide(hi-lo,hi,out=np.zeros_like(hi),where=hi>0)
        available=(light>=(.60 if number=='042' else .65))&(light<.915)&(sat>.105)
        for sy,sx in zip(*np.nonzero(available)):
            if not available[sy,sx]:continue
            available[sy,sx]=False;queue=deque([(sy,sx)]);points=[]
            while queue:
                y,x=queue.popleft();points.append((y,x))
                for yy,xx in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
                    if 0<=yy<available.shape[0] and 0<=xx<available.shape[1] and available[yy,xx]:
                        available[yy,xx]=False;queue.append((yy,xx))
            if not 80<=len(points)<=22000:continue
            yy,xx=np.array(points).T
            # A cropped background/container touches the ROI; never paint it.
            if yy.min()==0 or xx.min()==0 or yy.max()==available.shape[0]-1 or xx.max()==available.shape[1]-1:continue
            if xx.max()-xx.min()<9 or yy.max()-yy.min()<9:continue
            if number=='018':
                bw,bh=xx.max()-xx.min()+1,yy.max()-yy.min()+1
                if not (.65<=bw/bh<=1.55 and .65<=len(points)/(bw*bh)<=.89):continue
            if number=='020':
                # The solid feature bars and encoder polygons are convex.
                # Fill small historical highlight gaps inside each row, while
                # retaining the original component's outer edge and outline.
                filled=[(int(y),x) for y in np.unique(yy)
                        for x in range(int(xx[yy==y].min()),int(xx[yy==y].max())+1)]
                yy,xx=np.array(filled).T
            # Median source hue suppresses accidental hue noise within a glyph.
            median=np.median(a[yy,xx],axis=0)
            import colorsys
            hue=colorsys.rgb_to_hsv(*median)[0]
            name='green' if .16<=hue<.47 else ('yellow' if .04<=hue<.16 else ('red' if hue>=.90 or hue<.04 else ('purple' if .70<=hue<.90 else 'blue')))
            if number=='042':
                cx=x0+(xx.min()+xx.max())/2
                if 260<=cx<=340 or 1010<=cx<=1050 or 1220<=cx<=1280 or 1550<=cx<=1610 or y0>=678:name='yellow'
            color=restore.rgb(restore.PALETTE[name][0]).astype(np.uint8)
            out[y0+yy,x0+xx,:3]=color
            changes.append(dict(bounds=[int(x0+xx.min()),int(y0+yy.min()),int(x0+xx.max()+1),int(y0+yy.max()+1)],pixels=len(yy),main_color=restore.PALETTE[name][0]))
    return Image.fromarray(out),changes

def palette(im, rectangles):
    """Continuous, monotone lightness transfer, including activation intensities.

    Unlike the first transfer, no broad interval collapses to a single main or
    pale value. Original neutral ink stays neutral. Photos remain byte-exact.
    """
    rgba = np.array(im.convert('RGBA')); a = rgba[:,:,:3].astype(np.float32)/255
    hi=a.max(2); lo=a.min(2); delta=hi-lo; light=(hi+lo)/2
    sat=np.divide(delta,hi,out=np.zeros_like(hi),where=hi>0)
    r,g,b=a[:,:,0],a[:,:,1],a[:,:,2]; hue=np.zeros_like(hi); nz=delta>0
    for j,c in enumerate([r,g,b]):
        mask=nz&(hi==c)
        hue[mask]=[((g-b)/np.maximum(delta,1e-7))%6,
                   (b-r)/np.maximum(delta,1e-7)+2,
                   (r-g)/np.maximum(delta,1e-7)+4][j][mask]
    hue/=6; family=np.zeros_like(hi,dtype=np.uint8)
    family[(hue>=.16)&(hue<.47)]=1
    family[(hue>=.04)&(hue<.16)]=2
    family[(hue>=.90)|(hue<.04)]=3
    family[(hue>=.70)&(hue<.90)]=4
    protected=np.zeros_like(hi,dtype=bool); h,w=hi.shape
    for x0,y0,x1,y1 in rectangles:
        protected[round(y0*h):round(y1*h),round(x0*w):round(x1*w)]=True
    # Smooth coverage avoids discontinuities in pale fills and anti-aliasing.
    blend=np.clip((light-.55)/.30,0,1);blend=blend*blend*(3-2*blend)
    coverage=(1-blend)*np.clip((sat-.12)/.10,0,1)+blend*np.clip((sat-.02)/.08,0,1)
    coverage[protected]=0
    paint=a*255
    for j,name in enumerate(restore.PALETTE):
        main=restore.rgb(restore.PALETTE[name][0]); pale=restore.rgb(restore.PALETTE[name][1])
        # Main-color anchor .65 matches solid objects in model volumes; pale .95.
        # Knots stay strictly ordered to preserve quantitative lightness levels.
        t=np.clip((light-.65)/.30,0,1)
        target=main*(1-t[:,:,None])+pale*t[:,:,None]
        dark=np.clip(.55+light*(.45/.65),0,1); target*=dark[:,:,None]
        white=np.clip((light-.95)/.05,0,1)
        target=target*(1-white[:,:,None])+255*white[:,:,None]
        use=(coverage>0)&(family==j)
        paint[use]=target[use]*coverage[use,None]+paint[use]*(1-coverage[use,None])
    out=rgba.copy();out[:,:,:3]=np.rint(paint).clip(0,255).astype(np.uint8)
    assert np.array_equal(out[protected],rgba[protected])
    return Image.fromarray(out)

def rect(a):
    return [min(b[0] for b in a['boxes']),min(b[1] for b in a['boxes']),
            max(b[2] for b in a['boxes']),max(b[3] for b in a['boxes'])]

def resize(a, size):
    factor=size/max(s['size'] for s in a['segments'])
    for s in a['segments']:s['size']*=factor;s['dy']*=factor

def add(text,x,y,size=32,color=INK,kind='cn'):
    return dict(center_x=x,baseline_y=y,segments=[run(text,kind,size)],color=color)

def adjust(number, labels):
    # Primary labels use real neutral ink; group colors stay in the artwork.
    for a in labels:
        if a.get('color','').upper()!='#FFFFFF':a['color']=INK
    if number=='005':
        for i in [9,11]:labels[i]['center_x']=539
        for i in [20,21]:labels[i]['center_x']=800
    elif number=='014':
        labels[17]['baseline_y']=617
    elif number=='026':
        labels[7]['baseline_y']=466
    elif number=='046':
        labels[1]['baseline_y']=525
    elif number=='051':
        for i,x in enumerate([262,818,1374]):
            labels[i].update(center_x=x,baseline_y=76);resize(labels[i],36)
        for i in range(3,6):labels[i]['left_x']=238;resize(labels[i],34)
        for i in range(6,12):labels[i]['left_x']=787;resize(labels[i],32)
        for i in range(12,18):labels[i]['left_x']=1345;resize(labels[i],32)
        for row,(y0,y1) in enumerate([(207,255),(473,521),(735,783)]):
            labels[3+row]['baseline_y']=(y0+y1)/2
            for start in [6,12]:
                labels[start+2*row]['baseline_y']=y0
                labels[start+2*row+1]['baseline_y']=y1
    elif number=='069':
        labels[0]=add('相同初始收件箱：',887,66,32)
        labels.append(add('星标内容应保留',887,101,30))
        for i in [1,2]:labels[i]['baseline_y']=390;resize(labels[i],34)
        for i,x in [(3,653),(4,1130),(5,1533)]:
            labels[i].update(center_x=x,baseline_y=692);resize(labels[i],30)
        labels[6].update(center_x=298,baseline_y=817);resize(labels[6],32)
    elif number=='067':
        labels[6].update(center_x=214,baseline_y=602);resize(labels[6],34)
        for i in [7,8,9,10,13,14,15,16,17,18]:resize(labels[i],34)
        labels[10]['baseline_y']=975
        labels[12].update(center_x=405,baseline_y=2228);resize(labels[12],34)
        labels[14]['baseline_y']=1950
        labels[15]['baseline_y']=2090
        labels[16].update(center_x=418,baseline_y=1861)
        labels[17].update(center_x=418,baseline_y=2052)
        labels[18]['baseline_y']=1881
    elif number=='072':
        labels[0]=add('偏好对：同一提示下，更偏好与不偏好的回答',725,59,27)
        for i,x in [(1,197),(2,1228)]:labels[i].update(center_x=x,baseline_y=308);resize(labels[i],30)
        labels[3].update(center_x=431,baseline_y=510);resize(labels[3],27)
        labels[4]=add('固定奖励模型',363,549,26)
        labels.append(add('评分',363,581,26))
        labels[5].update(center_x=235,baseline_y=611);resize(labels[5],27)
        labels[6].update(center_x=415,baseline_y=755);resize(labels[6],27)
        labels[7].update(center_x=649,baseline_y=622);resize(labels[7],27)
        labels[8].update(center_x=580,baseline_y=699,color='#FFFFFF');resize(labels[8],32)
        labels[9].update(center_x=401,baseline_y=850);resize(labels[9],27)
        labels[10].update(center_x=234,baseline_y=946);resize(labels[10],27)
        labels[11].update(center_x=582,baseline_y=943);resize(labels[11],27)
        labels[12].update(center_x=798,baseline_y=485);resize(labels[12],27)
        labels[13].update(center_x=877,baseline_y=620);resize(labels[13],27)
        labels[14].update(center_x=1222,baseline_y=620);resize(labels[14],27)
        labels[15].update(center_x=1130,baseline_y=789);resize(labels[15],27)
        labels[16].update(center_x=1036,baseline_y=943);resize(labels[16],27)
        labels[17].update(center_x=725,baseline_y=1034);resize(labels[17],27)
    elif number=='080':
        labels[16]['center_x']=1170
    elif number=='089':
        for i,x,y in [(5,558,318),(6,1107,317),(13,432,645),(14,1143,627),(15,1354,667)]:
            labels[i].update(center_x=x,baseline_y=y)
        resize(labels[15],25)
        labels[18]['baseline_y']=758
    # Current terminology is an editable overlay; historical label sources stay
    # unchanged so the pre-commit design remains exactly reproducible.
    common={'训练集':'训练样本','验证集':'验证样本','测试集':'测试样本',
            '辅助训练数据':'辅助训练样本','训练数据':'训练样本',
            '独立训练数据':'独立训练样本','校准数据':'校准样本',
            '学习算法':'学习映射','同一算法':'同一学习映射'}
    specific={
        '010':{1:('使用','预测'),10:('新输入','预测输入'),11:('模型','训练模型')},
        '017':{0:('带标签集合','带标签训练样本'),5:('加入带标签集','加入训练样本')},
        '019':{8:('损失','目标'),9:('损失','目标')},
        '020':{6:('目标模型','目标训练模型')},
        '021':{6:('检查损失','检查目标'),11:('检查损失','检查目标'),16:('检查损失','检查目标')},
        '022':{1:('输入','预测输入'),2:('当前模型','当前参数'),8:('后续输入','后续预测输入'),
               10:('输入','预测输入'),11:('固定模型','固定参数'),13:('输入','预测输入'),
               14:('固定模型','固定参数'),16:('输入','预测输入'),17:('固定模型','固定参数')},
        '023':{4:('本地数据','本地训练样本'),8:('本地数据','本地训练样本'),12:('本地数据','本地训练样本')},
        '025':{2:('新观测','独立评价记录')},
        '026':{24:('四个输入等概率','四种预测输入等概率')},
        '032':{7:('同一测试点','同一评价记录')},
        '033':{8:('输出','训练结果')},
        '036':{4:('选解算法','选解规则')},
        '040':{1:('输入','训练特征'),2:('输入','预测输入')},
        '042':{2:('输入','预测输入'),5:('输出','预测输出'),11:('输出','预测输出')},
        '043':{6:('损失','目标值'),7:('损失','目标值'),8:('扰动平均损失','扰动平均目标值'),9:('扰动平均损失','扰动平均目标值')},
        '046':{1:('无标签目标输入','无标签目标样本'),31:('输入','预测输入')},
        '055':{8:('同一输入','同一预测输入')},
        '059':{5:('新输入','新预测输入')},
        '062':{1:('原输入','原预测输入')},
        '076':{1:('干净输入','干净预测输入'),5:('相同的损坏输入','同一损坏预测输入'),9:('相同的损坏输入','同一损坏预测输入')},
        '081':{1:('公开输入','公开训练特征'),16:('公开输入','公开训练特征')},
        '083':{0:('原数据','原训练样本'),3:('旧模型','原训练模型'),
               5:('比较输出分布','比较发布模型分布'),7:('保留数据','保留训练样本'),
               10:('精确遗忘要求输出同分布','精确遗忘要求发布模型同分布')},
        '084':{1:('含被修改记录的训练样本','含修改记录的训练样本'),12:('干净输入','干净预测输入')},
        '072':{17:('偏好数据','偏好训练样本')},
    }
    for i,a in enumerate(labels):
        for s in a['segments']:
            for before,after in common.items():s['text']=s['text'].replace(before,after)
            if i in specific.get(number,{}):
                before,after=specific[number][i];s['text']=s['text'].replace(before,after)
    if number=='032':
        for i in [0,1,3,4]:resize(labels[i],34)
        for i in [1,4]:
            for s in labels[i]['segments']:s['text']=s['text'].replace('同一学习映射','学习映射')
    if number=='083':
        labels[5]=add('比较发布模型分布',1150,515,27)
    return labels

def main(only=None):
    path=HERE/'restoration-report.json';report=json.loads(path.read_text())
    log=json.loads((HERE/'refinement-check.json').read_text()) if only else []
    if only:log=[r for r in log if r['id'] not in only]
    for row in report['records']:
        number=row['id']
        if only and number not in only:continue
        if number=='085' or row.get('model_redraw_20261013'):continue
        folder=ROOT/row['asset'];folder=folder.parent
        labels=json.loads((folder/'restored-design-labels.json').read_text())
        background=Image.open(folder/'restored-design-background.png').convert('RGBA')
        original_background=background.copy()
        background=palette(background,restore.PHOTOS.get(number,[]))
        background,primary_changes=emphasize_primary(original_background,background,number)
        extra=None
        original=Image.open(folder/'restored-design-original.png').convert('RGBA')
        if number=='002':
            padded=Image.new('RGBA',original.size,'white');padded.paste(background,(0,0));background=padded
        elif original.height>background.height:
            extra=palette(original.crop((0,background.height,original.width,original.height)),[])
        if number=='067':
            background,labels,_=restore.vertical(background,labels)
            # Give the second threshold label the same interior clearance as
            # the first: extend only the lower edge of its containing frame.
            edge=background.crop((382,2055,595,2056))
            bottom=background.crop((382,2056,595,2085))
            background.paste('white',(382,2056,595,2116))
            for y in range(2056,2087):background.paste(edge,(382,y))
            background.paste(bottom,(382,2087))
        labels=adjust(number,labels)
        background.save(folder/'refined-background.png')
        t=Typeset(folder/'refined-background.png',folder,ROOT/'fonts')
        for a in labels:
            x=a['center_x']
            if 'left_x' in a:
                width=sum(t.draw.textlength(s['text'],font=t.font(s['font'],s['size'])) for s in a['segments'])/SCALE
                x=a['left_x']+width/2
            t.text(x,a['baseline_y'],a['segments'],a['color'])
        t.save()
        if extra is not None:
            top=Image.open(folder/'figure.png').convert('RGBA')
            full=Image.new('RGBA',(top.width,top.height+extra.height),'white')
            full.paste(top,(0,0));full.paste(extra,(0,top.height));full.convert('RGB').save(folder/'figure.png',dpi=(300,300))
        overlaps=[]
        for (i,a),(j,b) in itertools.combinations(enumerate(t.labels),2):
            aa,bb=rect(a),rect(b);dx=min(aa[2],bb[2])-max(aa[0],bb[0]);dy=min(aa[3],bb[3])-max(aa[1],bb[1])
            if dx>0 and dy>0:overlaps.append([i,j,round(dx,2),round(dy,2)])
        check=json.loads((folder/'typography-check.json').read_text())
        ppp=row['body_width_mm']/25.4*72/background.width
        check.update(width_mm=row['body_width_mm'],minimum_primary_pt=min(max(s['size'] for s in a['segments'])*ppp for a in t.labels),label_pair_overlaps=overlaps,check_basis='Re-rendered real-font text layers; explicit alignment and spacing; publication size.',background_artwork_geometry='original; only palette transfer and documented 067 translations')
        (folder/'typography-check.json').write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n')
        row['initial_color_check']=row.get('initial_color_check',row.get('check'))
        row['check']={'missing_glyphs':check['missing_glyphs'],'outside_canvas':check['outside_canvas'],'minimum_primary_pt':check['minimum_primary_pt'],'label_pair_overlaps':overlaps,'photo_background_pixels':'unchanged within declared rectangles'}
        row['layout_refinements']='label positions and sizes corrected where needed; 067 lower threshold frame extended 31 pixels with original rounded edge'
        row['primary_color_emphasis']=primary_changes
        row.update(sha256=restore.sha((folder/'figure.png').read_bytes()),font_policy='Real fonts re-rendered in neutral ink; publication size and alignment checked.',refinement_renderer=str(Path(__file__).resolve().relative_to(ROOT)),refinement='Continuous lightness transfer; new editable text layer; manual layout corrections where recorded.')
        (folder/'restoration-20261013.json').write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n')
        settings=json.loads((folder/'typesetting.json').read_text());settings.update(background='refined-background.png',labels_source='labels.json',text_layer='text-layer.png',renderer=str(Path(__file__).resolve().relative_to(ROOT)))
        (folder/'typesetting.json').write_text(json.dumps(settings,ensure_ascii=False,indent=2)+'\n')
        log.append(dict(id=number,minimum_primary_pt=check['minimum_primary_pt'],overlaps=overlaps,manual_layout=number in ['014','026','046','051','069','067','072','080','089']))
        print(number,'min pt',round(check['minimum_primary_pt'],2),'overlaps',overlaps,flush=True)
    path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    (HERE/'refinement-check.json').write_text(json.dumps(sorted(log,key=lambda r:r['id']),ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':main()
