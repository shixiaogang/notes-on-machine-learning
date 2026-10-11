# Human-selected wording repairs after the three separate reading passes.
import json,re,hashlib
from pathlib import Path
b=Path(__file__).parent;u=json.loads((b/'v1-units.json').read_text());f=Path(u['file']);t=f.read_text()
replacements={
65:[('固定图像输入$\\bm{x}\\in[0,1]^d$','固定像素已缩放到$[0,1]$的图像输入$\\bm{x}\\in[0,1]^d$')],
75:[('配对初始化和超参数，多随机种子重复','采用配对初始化和超参数，在多个随机种子下重复')],
81:[('另报全部非目标样本','另行报告全部非目标样本')],
104:[('用独立查询集之外的任务输入测一致率和任务效用','用与查询集独立的任务输入测量一致率和任务效用')],
112:[('分别判用户任务及攻击目标','分别判断用户任务完成与攻击目标达成')],
113:[('$B\\not\\subseteq A$判提案越权，$C\\not\\subseteq A$判执行端允许越权','$B\\not\\subseteq A$表示提案越权，$C\\not\\subseteq A$表示执行端允许越权')],
114:[('无法自动判的案例','无法自动判断的案例')],
121:[('材料准入先核数据来源','材料准入先核查数据来源')],
123:[('核主体及数量','核验主体及数量'),('前两类验权限执行，后一类验内容审查','前两类检查权限规则是否执行，后一类检查内容审查能否发现污染')],
135:[('换攻击面时须重定假设','换攻击面时须重新明确适用假设')],
141:[('可清污染材料并从可信起点重训','可以清理受污染材料并从可信起点重训')],
142:[('剪枝可能伤任务','剪枝可能损害正常任务')],
151:[('少给反馈、限制查询','减少反馈信息、限制查询')],
153:[('在独立输入上比一致率，再核正常任务损失','在独立输入上比较功能一致率，再检查正常任务损失')],
160:[('多层措施还要核共同弱点','多层措施还要检查共同弱点')],
161:[('前者核规则，后者查模型、路由及执行器旁路','前者检验授权规则，后者检查模型、路由及执行器旁路')],
164:[('再结合状态及独立记录判是否处置','再结合状态及独立记录判断是否需要处置')],
165:[('仅拒当前输入清不掉参数或记忆污染','仅拒绝当前输入，不能清除参数或记忆中的污染')],
166:[('限动作规模','限制动作规模')],
167:[('检查停后续、撤权与标签恢复','检查后续动作是否停止、权限是否撤销及标签是否恢复'),('外发信息只可验后续传播是否受限，本地删日志不等于收回','已经外发的信息只能检查后续传播是否受限，在本地删除日志不等于收回信息')],
168:[('仅换模型而留入口，或仅删文档而不查记忆及派生状态','仅替换模型却保留注入入口，或仅删除文档却不检查记忆及派生状态')],
171:[('来源检查拦未获准材料','来源检查可以拦截未获准材料')]
}
blocks=[]
for p in u['blocks']:
 n=int(p['id'][-3:]);text=p['text']
 for a,z in replacements.get(n,[]): assert a in text,(n,a);text=text.replace(a,z)
 blocks.append(text)
out='\n\n'.join(blocks)+'\n';f.write_text(out);(b/'snapshots/v2').mkdir(exist_ok=True);(b/'snapshots/v2'/f.name).write_text(out)
u2={'file':str(f),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'blocks':[]}
for i,m in enumerate(re.finditer(r'\S(?:.*?\S)?(?=\n\s*\n|\Z)',out.rstrip(),re.S),1):
 p={'id':f'08-P{i:03}','line':out.count('\n',0,m.start())+1,'text':m.group(),'sentences':[]}
 for s in re.findall(r'[^。！？]*[。！？]|[^。！？]+$',m.group()):
  if re.search(r'[一-龥]',s):p['sentences'].append({'id':p['id']+f'-S{len(p["sentences"])+1:02}','text':s.strip()})
 u2['blocks'].append(p)
(b/'v2-units.json').write_text(json.dumps(u2,ensure_ascii=False,indent=2)+'\n')
print(u2['sha256'],'P=',len(u2['blocks']),'S=',sum(len(p['sentences']) for p in u2['blocks']))
