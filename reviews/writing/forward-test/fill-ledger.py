from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import shutil
import subprocess

base = Path(__file__).resolve().parent
manifest = json.loads((base / 'input-manifest.json').read_text())
catalog = json.loads((base / 'inputs/skill/references/review-criteria.json').read_text())
record = json.loads((base / 'review-r1.json').read_text())
paragraph = (base / 'inputs/paragraph.tex').read_text().strip()
sentences = [s + '。' for s in paragraph.split('。') if s]
assert len(sentences) == 5
units = [f'P1.S{i}' for i in range(1, 6)]

def evidence(quote, explanation, unit='P1'):
    assert quote in paragraph
    return {'artifact': 'source', 'quote': quote,
            'locator': f'{unit}；第30行；以短引定位', 'explanation': explanation}

def ev_for(unit_numbers, explanation):
    return [evidence(sentences[i-1], explanation, f'P1.S{i}') for i in unit_numbers]

def sub(requirement_id, status, action, reason, ns, missing=None, scope_basis=None):
    value = {'requirement_id': requirement_id, 'status': status,
             'units': [f'P1.S{i}' for i in ns],
             'applicable_units': [f'P1.S{i}' for i in ns],
             'performed_action': action, 'reason': reason,
             'evidence': ev_for(ns, reason), 'findings': ['F01'] if status == 'fail' else []}
    if missing:
        value['missing'] = missing
    if scope_basis:
        value['scope_basis'] = scope_basis
    return value

record.update({'record_id': 'AW-FORWARD-ROBUSTNESS-20261010', 'revision': 'R1', 'date': '2026-10-10',
               'reviewer': {'name': 'rule_workflow_forward_test',
                            'role': '独立 AI 子代理试读；未参与本段及相关上下文改写；非真实读者实验'},
               'recoverable': {'kind': 'snapshot', 'path': 'snapshots/review-r1.json'}})
version = 'git:' + manifest['source_HEAD']
source = {'kind': 'source', 'path': 'inputs/03-robustness.tex', 'version': version,
          'sha256': manifest['source_sha256'],
          'recoverable': {'kind': 'git',
                          'root': '/Users/bytedance/Projects/notes_on_machine_learning/.worktrees/volumes-one-two-prose-review',
                          'commit': manifest['source_HEAD'],
                          'path': 'tex/02-foundations/03-trustworthiness/03-robustness.tex'}}
record['artifacts'] = {'source': source}
record['scope'] = {'target': '只读第30行局部扰动段，逐句审读五句并试用三个通用写作规则，禁止修改书籍正文',
                   'targets': [{'artifact': 'source', 'path': source['path'], 'sha256': source['sha256'],
                                'version': version, 'range': '第30行，P1.S1—P1.S5'}],
                   'reader': '已懂分类和平均错误率、初学鲁棒性的读者',
                   'required_criteria': ['LG03', 'LG06', 'LG11'],
                   'not_read': ['相邻段落', '所在小节标签', 'sec:distribution-shift节', '旧章节12审读记录',
                                '现成缺陷答案', '外部文献', '图源', 'PDF'],
                   'limitations': '不判断全章是否已解释术语，不查引用目标，不执行项目规则表，不修改或构建正文。'}
record['sentence_coverage'] = [
    {'unit': 'P1.S1', 'quote': sentences[0], 'judgment': '接受局部扰动的范围限定；含义与承前预期待核Q02。'},
    {'unit': 'P1.S2', 'quote': sentences[1], 'judgment': '接受分类后续入口；具体对象和信息要求用途待核Q03。'},
    {'unit': 'P1.S3', 'quote': sentences[2], 'judgment': '接受符号对应先给对象；风险与平均错误率的桥接及环境含义待核Q02。'},
    {'unit': 'P1.S4', 'quote': sentences[3], 'judgment': '允许环境量词和原环境基准在附近；下降的指标对象不唯一F01。'},
    {'unit': 'P1.S5', 'quote': sentences[4], 'judgment': '接受始终很差也可变化很小的反例；仍未消除下降指标歧义F01。'}]
record['findings'] = {
    'F01': {'status': 'open', 'kind': '局部理解障碍', 'units': ['P1.S4', 'P1.S5'],
            'before': [evidence('相对于原环境的下降不超过给定幅度', '前半的风险与末句的表现是不同可恢复对象。', 'P1.S4'),
                       evidence('绝对风险和下降幅度需要一起看', '并列的是风险水平与省略指标的下降幅度，后一对象仍不唯一。', 'P1.S5')],
            'reason': '下降可承前指风险，也可由后句理解为预测表现；对已懂平均错误率的读者，会影响改善和恶化方向。',
            'recommended_action': '明确指标对象及方向；若沿用风险解释增加量，若沿用表现明确其指标及与风险对应，不擅自选择。',
            'revision_evidence': '未修改', 'reread_evidence': '仅复核原段S3—S5，未生成改后版本，不关闭问题。'},
    'Q02': {'status': 'open', 'kind': '待核上下文，不断言全章遗漏', 'units': ['P1.S1', 'P1.S3', 'P1.S4'],
            'before': [evidence('环境$e$中的风险记为$R_e(f)$', '只有环境/风险与符号的对应，没有已知平均错误率的桥接。', 'P1.S3')],
            'reason': '前文是否已解释局部扰动、分布变化、环境、风险及允许环境未读。',
            'recommended_action': '授权扩展后找首次定义和准确回指，再判断是否需要局部补充。',
            'revision_evidence': '未修改', 'reread_evidence': '未执行前后文核验，不关闭。'},
    'Q03': {'status': 'open', 'kind': '待核上下文与分类目标', 'units': ['P1.S2'],
            'before': [evidence('具有不同的信息要求', '无法知道需要什么信息、用于识别变化还是估计风险或适应环境。', 'P1.S2')],
            'reason': '三个变化名称没有当前可复述的对象与信息用途；后续分类未检查。',
            'recommended_action': '先核查前文及所指分类是否提供解释；不直接把后续分类迁回本段。',
            'revision_evidence': '未修改', 'reread_evidence': '未执行目标节核验，不关闭。'}}

checks = {c['criterion_id']: c for c in record['checks']}
checks['LG03'].update({'status': 'fail', 'units': units, 'applicable_units': units,
    'applicability': '五句均为普通连续正文；S4有主语与变化对象的承前省略。',
    'performed_action': '逐句拆出对象—动作—关系；恢复S4也可以要求的主语为鲁棒性；对照S3风险与S5表现为下降寻找唯一对象。',
    'reason': '主语省略可恢复，下降的对象不能唯一恢复；F01是当前片段的问题，不断言全章缺定义。',
    'evidence': ev_for([1,2,3,4,5], '已逐句记录对象与动作；只有S4—S5的下降对象存在可改变指标方向的多解。'),
    'findings': ['F01']})
checks['LG03']['subchecks'] = [
    sub('LG03.375195e26b','fail','逐句列出对象、动作和关系，比较S4下降的两个先行对象。','S4—S5的下降可指风险或表现，关系不能唯一恢复。',[1,2,3,4,5]),
    sub('LG03.04347cf7c9','pass','逐句查是否是仅有动作的提纲碎片。','S1有范围判断，S2有分类与引用，S3有符号指派，S4有两种要求，S5有解释反例；没有只有动作标签的碎片。',[1,2,3,4,5]),
    sub('LG03.84b19b3f21','not_applicable','通读五句查操作步骤或提纲动作片段。','这段是概念边界与评价比较，没有先固定/再看一类操作步骤；不为此添加流程。',[1,2,3,4,5]),
    sub('LG03.53dbc163ca','pass','为也可以要求恢复省略主语。','也可以要求承接同句的鲁棒性可以要求，主语唯一。',[4]),
    sub('LG03.182541a425','fail','区分可恢复的主语与变化对象，追踪下降。','无需重复鲁棒性主语，但下降缺少可唯一恢复的指标对象。',[4,5]),
    sub('LG03.ca36b5c6c4','not_applicable','核对片段类型。','所读只有一段正文五句，没有标题、表头或算法步骤。',[1,2,3,4,5]),
    sub('LG03.fae1c0f40f','not_applicable','查找只有动作标签的句子。','各句都有对象和判断；问题是指标省略而不是只有再看容量式标签。',[1,2,3,4,5]),
    sub('LG03.e2d2578728','not_applicable','比较五句主语及同句省略。','主语随局部扰动、三类变化、风险、鲁棒性、两个评价量变化，没有机械重复同一主语的触发情形。',[1,2,3,4,5]),
    sub('LG03.c2f5f70509','not_applicable','核对被审对象是否是该模型族改写示例或实际修订。','这条原句解释特定示例的改写结果；本段不讨论固定任务与模型族，也没有实际改写，不把示例结果泛化为本文任务。',[1,2,3,4,5]),
    sub('LG03.a87c78c734','not_applicable','核對原文与任务是否发生三短句合并。','本测试不改正文，没有该示例的三个短句或拼句操作；不声称已经通过修改消除缺口。',[1,2,3,4,5]),
    sub('LG03.940320d4e5','out_of_scope','已定位S4对象缺口，登记条件性最小修改动作；核对任务边界。','诊断已经完成，补写正文和放回前后文复读属于实际修订，未执行。',[4,5],scope_basis='父代理明确要求不修改书籍正文，只读指定段落，记录存临时目录。'),
    sub('LG03.05d6f6faa2','pending','重建P1作用并查S4—S5比较关系，追踪S1并未的承前依据。','本段评价比较可重建，F01已定位；前段未读，S1承前预期不能核验。',[1,4,5],missing='缺P1前段和全章范围；不从局部推断全部段落关系。')]

lg06_units = [units[i-1] for i in [1,3,4,5]]
checks['LG06'].update({'status':'pass','units':lg06_units,'applicable_units':lg06_units,
    'applicability':'S1、S3、S4、S5含范围/环境/比较基准/程度限制；S2没有嵌套定语或成立条件作用域。',
    'performed_action':'逐一配对全部→分布变化，环境e→风险，所有→允许环境，相对于原环境→下降，给定幅度→下降上限，始终→表现很差，几乎→没有下降；检查定语链长度与条件位置。',
    'reason':'这些限制词作用域在本段唯一且与判断相邻；只验收修饰范围，没有验收风险定义或下降指标的含义。',
    'evidence':ev_for([1,3,4,5],'限定词紧邻所限定的集合、环境、比较基准或程度，不会被读成无条件全环境保证。'),
    'findings':[]})
checks['LG06'].pop('missing',None)
checks['LG06']['subchecks'] = [
    sub('LG06.f4cbacc7fe','not_applicable','拆出两个短定语链并查有无层层套叠。','所有允许环境的风险、相对于原环境的下降均为短链；没有过长的的字链需要拆开。',[3,4]),
    sub('LG06.11eaec05b5','pass','核对句首讨论对象与随后限定的先后。','先出现局部扰动、风险、鲁棒性要求和评价量，再给范围、环境、容限或示例；通过限于句法对象位置，F01语义歧义另记。',[1,3,4,5]),
    sub('LG06.d0ad8fa0ad','pass','把允许环境、原环境基准和给定幅度与各判断配对。','绝对要求限定在允许环境内，相对要求就近给原环境基准和给定幅度，条件没有远离判断。',[4]),
    sub('LG06.96acc3e236','pass','标出全部、所有、始终、几乎的被限定项。','全部限定分布变化，所有限定允许环境，始终限定模型表现很差，几乎限定没有下降；不把后两者当作精确实验数值。',[1,4,5])]

checks['LG11'].update({'status':'fail','units':[units[i-1] for i in [2,3,4,5]],
    'applicable_units':[units[i-1] for i in [2,3,4,5]],
    'applicability':'S2承载信息要求抽象标签，S3引入风险，S4—S5比较绝对要求和相对变化。',
    'performed_action':'尝试复述两种要求的比较对象及判别标准，用S5反例检验；回查S2信息要求及S3风险能否就地解释，保留未知前文。',
    'reason':'绝对标准是环境风险容限，后一标准的指标对象不唯一，无法实际区分其方向；信息要求与术语桥接仍待前文核查。',
    'evidence':ev_for([2,3,4,5],'S4—S5提供对照和反例但未命名相对下降指标；S2标签信息及用途未在片段中可复述。'),
    'findings':['F01','Q02','Q03']})
checks['LG11']['subchecks'] = [
    sub('LG11.f529be0245','fail','写出绝对容限和相对变化分别考察什么，用末句反例检查区别。','第一要求考察风险水平；第二下降对象可为风险或表现，F01使比较指标方向不能确定。',[4,5]),
    sub('LG11.a2b4803785','pending','把信息要求和风险改述为考察什么的问题，查本段是否提供答案。','信息用于何任务、风险如何对应平均错误率不能仅凭本段回答；不凭术语熟悉自动补齐。',[2,3],missing='未读前文的解释或交叉引用入口，不能确认首次引入是否已有支持。'),
    sub('LG11.3318c9ee0b','pending','核对信息要求所指对象及判断标准，保留模型族/接口仅为例子。','本段关键标签信息要求没有具体信息与用途；前文或分类目标可能已有解释，尚未核查。',[2],missing='缺已授权范围之外的前文与分类目标正文。'),
    sub('LG11.fff8791a04','pending','核对本段是否承担多维组合分类，定位分类后续入口。','只见三类变化名称及后续分类入口，不能判定后文是否是多维比较或缺必要组合说明；表格是可选表达，不要求此段加表格。',[2],missing='未读后续分类，适用条件及组合约束待核。')]

for check in [checks['LG03'],checks['LG11']]:
    check.pop('missing',None)
record['conclusions']={'record':'needs_review','text':'needs_revision',
    'record_reason':'已完成五句证据与三个规则动作记录，待另一代理对实际输入复核；不冒称独立记录复审。',
    'text_reason':'仅受审片段F01待修改；Q02和Q03待上下文核查。未修改，未关闭发现。'}
(base / 'snapshots').mkdir(exist_ok=True)
raw=json.dumps(record,ensure_ascii=False,indent=2)+'\n'
(base / 'review-r1.json').write_text(raw)
(base / 'snapshots/review-r1.json').write_text(raw)
for name in ['review-r1.md','usability-r1.md']:
    shutil.copy2(base/name,base/'snapshots'/name)

# 保留未锁定版本日志；单独调用台账函数只为分辨其错误来源。
spec=importlib.util.spec_from_file_location('record_checker',base/'inputs/skill/scripts/check_review_records.py')
checker=importlib.util.module_from_spec(spec); spec.loader.exec_module(checker)
errors=checker.check_record(record,catalog,(base/'inputs/skill/references/review-criteria.json').read_bytes(),base,
                            (base/'review-r1.json').read_bytes(),base/'review-r1.json')
(base/'ledger-only-check-r1.log').write_text('台账自身字段核验；不包含catalog核验，也不代表独立阅读复审。\n'+ ('\n'.join(errors) if errors else '0 errors')+'\n')
assert not errors, errors

# 新锁定输入另存，与旧版保持隔离；重审三项的内容和子要求映射变化。
locked_original=Path('/private/tmp/aw-rule-audit-final-input-r3')
locked=base/'inputs/locked-r3'; locked.mkdir(exist_ok=True)
new_catalog=json.loads((locked_original/'catalog.json').read_text())
shutil.copy2(locked_original/'catalog.json',locked/'catalog.json')
for s in new_catalog['sources']:
    target=locked/s['path']; target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(locked_original/s['path'],target)
changes=[]
for cid in ['LG03','LG06','LG11']:
    old=next(c for c in catalog['criteria'] if c['id']==cid)
    new=next(c for c in new_catalog['criteria'] if c['id']==cid)
    changes.append({'id':cid,'criterion_unchanged':old==new,
                    'old_requirement_count':len(old['requirements']),
                    'new_requirement_count':len(new['requirements'])})
    assert old==new, (cid,'需按变化重审')
new_record=copy.deepcopy(record)
new_record['revision']='R2'
new_record['catalog_sha256']=hashlib.sha256((locked/'catalog.json').read_bytes()).hexdigest()
new_record['recoverable']={'kind':'snapshot','path':'snapshots/review-r2.json'}
new_record['rebind']={'prior_record':'review-r1.json','new_catalog_path':'inputs/locked-r3/catalog.json',
                     'actual_action':'核对LG03、LG06、LG11动作和子要求完全相同；验证8份规则摘要与旧输入一致，保持原始逐句证据与判断。',
                     'criterion_comparison':changes,
                     'source_comparison':[]}
for s in new_catalog['sources']:
    old_hash=hashlib.sha256((base/'inputs/skill'/s['path']).read_bytes()).hexdigest()
    new_hash=hashlib.sha256((locked/s['path']).read_bytes()).hexdigest()
    new_record['rebind']['source_comparison'].append({'path':s['path'],'old_sha256':old_hash,'new_sha256':new_hash,'unchanged':old_hash==new_hash})
    assert old_hash==new_hash, (s['path'],'规则全文有变化需重读')
# 保留所有编号及新版未查子项；仅迁移实际试用的三项，其他重新由新版要求初始化pending。
tested={'LG03','LG06','LG11'}
new_record['checks']=[]
for c in new_catalog['criteria']:
    if c['id'] in tested:
        new_record['checks'].append(copy.deepcopy(checks[c['id']]))
    else:
        new_record['checks'].append({'criterion_id':c['id'],'status':'pending','units':[],
            'applicable_units':[],'performed_action':'','reason':'本次只试用LG03、LG06、LG11；此项尚未执行',
            'missing':'缺该规则的原文核对、实际动作、定位证据和具体判断；不从五句已读推定规则已查。',
            'evidence':[],'findings':[],
            'subchecks':[{'requirement_id':r['id'],'status':'pending','reason':'未执行此原文子要求',
                         'missing':'缺实际动作、定位证据及具体判断'} for r in c.get('requirements',[])]})
new_raw=json.dumps(new_record,ensure_ascii=False,indent=2)+'\n'
(base/'review-r2.json').write_text(new_raw)
(base/'snapshots/review-r2.json').write_text(new_raw)

for name,args in [
    ('catalog-check-r2.log',['catalog','--root','inputs/locked-r3','--catalog','inputs/locked-r3/catalog.json']),
    ('record-check-r2.log',['record','--root','inputs/locked-r3','--catalog','inputs/locked-r3/catalog.json','--record','review-r2.json'])]:
    result=subprocess.run(['python3','inputs/skill/scripts/check_review_records.py',*args],cwd=base,text=True,capture_output=True)
    (base/name).write_text(f'exit_code={result.returncode}\n'+result.stdout+result.stderr)
    print(name,'exit',result.returncode)
    if result.returncode:
        print(result.stdout+result.stderr)
print('R2 SHA:',new_record['catalog_sha256'])
print('Trial:',[(c['criterion_id'],c['status']) for c in new_record['checks'] if c['criterion_id'] in tested])
print('Untested pending:',sum(c['status']=='pending' for c in new_record['checks']))
