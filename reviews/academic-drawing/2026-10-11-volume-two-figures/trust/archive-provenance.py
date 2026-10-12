"""Archive actual image references and mechanical provenance; no review verdicts."""
from pathlib import Path
import subprocess, json, hashlib, shutil
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
BASE=ROOT/'figures/03-foundations/03-trustworthiness/generated'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def record(p,role,source):return {'file':str(p.relative_to(ROOT)),'sha256':sha(p),'role':role,'source':source}
SHARED=BASE/'references-20261011'
SHARED.mkdir(exist_ok=True)
specs={
 'multi-task-20261011.png':('volume-two-figures-basics','figures/03-foundations/01-basics/generated/multi-task-learning/background-20261011-r5.png','共享单一模型及反馈组织；纯白模块与低饱和细描边，不借用任务标签'),
 'pate-20261011.png':('volume-two-figures','figures/03-foundations/03-trustworthiness/generated/pate-private-teachers/background-20261011-r3.png','多分支汇合的层级与白底模块，不借用隐私机制'),
 'defense-20261011.png':('volume-two-figures','figures/03-foundations/03-trustworthiness/generated/defense-in-depth/background-20261011-r3.png','平面流程、细描边与白底；不借用防御语义')}
shared={}
for name,(tree,rel,role) in specs.items():
 src=ROOT.parent/tree/rel
 dest=SHARED/name
 shutil.copyfile(src,dest)
 shared[name]=record(dest,role,{'worktree':tree,'path':rel})
refs={
 'adversarial-training':['multi-task-20261011.png'],
 'fairness-opportunity':['defense-20261011.png'],
 'fairness-interventions':['multi-task-20261011.png','pate-20261011.png'],
 'rlhf-dpo-feedback':['multi-task-20261011.png','pate-20261011.png'],
 'activation-patching':['multi-task-20261011.png','pate-20261011.png']}
final={'adversarial-training':'background-20261011-r3.png','fairness-opportunity':'background-20261011-r4.png','fairness-interventions':'background-20261011-r6.png','rlhf-dpo-feedback':'background-20261011-r3.png','activation-patching':'background-20261011-r2.png'}
for key,names in refs.items():
 folder=BASE/key
 archive=folder/'references'
 archive.mkdir(exist_ok=True)
 dest=archive/'baseline-20261011.png'
 path=str((folder/'figure.png').relative_to(ROOT))
 dest.write_bytes(subprocess.check_output(['git','show','HEAD:'+path],cwd=ROOT))
 original=record(dest,'相同主题旧图，仅核对科学对象与关系；旧颜色、渐变、纹理与装饰不借用',{'commit':'b0ffa7ff754e0cb39ea261c2e680ff5c7ba38017','path':path})
 outputs=[{'file':p.name,'sha256':sha(p)} for p in sorted(folder.glob('background-20261011*.png'))]
 data={'date':'2026-10-11','tool':'image_gen.imagegen','model_name':'not exposed by tool','seed_and_generation_parameters':'not exposed by tool','initial_actual_reference_images':[original]+[shared[n] for n in names],'revision_inputs':'the preceding local wordless candidate; scientific brief and selected initial references remain the basis; exact input candidate identified by prompt revision order','outputs':outputs,'selected_background':final[key],'selected_sha256':sha(folder/final[key]),'processing':'No background cleanup, tracing, recoloring, cropping, scaling or blurring; actual font overlay only','prompt':'prompt-20261011.txt','typesetting_source':'../typeset_20261011.py','label_configuration':'typesetting-20261011.json','font_proof':'typography-20261011.json','review':'reviews/academic-drawing/2026-10-11-volume-two-figures/trust/figure-review.md'}
 (folder/'generation-20261011.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print('Archived references for',len(refs),'selected complex diagrams')
