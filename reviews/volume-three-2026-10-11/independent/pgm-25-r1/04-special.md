# I25-R1 特殊单元独立复核

与固定源同SHA。W后逐显示公式读其引句、整式、尾句；排版环境内中文标点不拆推理。45项均为手写；行范围取math.json仅作地址。

I25-M01（L40–42）：检验H0是给S后ij独立，S已排端点；回答能否暂删邻接，未拒的有限功效限制紧后给出。

I25-M02（L46–52）：G²比较联合频数与分层独立频数；只对正N项求和保证各边缘分母正，近似χ²的正性/固定状态/自由度在式后。每个s单层LL比乘2，无漏n系数。

I25-M03（L56–60）：条件MI用p(a,b,s)加权log条件比；解释为Σs p(s)KL，零p(s)层不贡献，E=0 iff有关支持上的CI。经验同计数等于G²/(2n)。

I25-M04（L64–68）：Fisher Z=√(n−|S|−3)atanh(partialrho)；用于Gaussian条件CI检验，非退化与n自由度条件在相邻句，sample|rho|=1退化不属正态近似适用范围。

I25-M05（L90–93）：36/50=45/50×40/50=.72；是给2=0的00一格，文本没有只用一格推出CI，随后明确余格均分解。

I25-M06（L101–107）：三对G²由同100记录复算为73.6128414、38.5489514、24.0180527，显示边缘皆依赖；给2后13为0，渐近临界值只演示PC操作。

I25-M07（L116–121）：完整自由CPT的MLElog分按node/parentrow/state求和；Nij零行另任选归一表、0log0项跳过，局部分解支持缓存和局部改父分数。

I25-M08（L125–133）：BIC=LL−klogn/2及k=Σqi(ri−1)，回答比拟合还扣什么代价；越大越好，−2后排序改最小化与regular证据条件清楚。

I25-M09（L141–150）：先验平均似然得到pD|G后乘pG归一posterior；任务由只最优θ转参数不确定。后BF段补总证据正有限，CPT行正先验可精确算。

I25-M10（L154–165）：BF分母证据正有限；posteriorodds还需pG2>0、总evidencepositive finite。两层先验区分，3×1/2=3/2数例值为赔率非单个prob。

I25-M11（L169–178）：Dir evidence为每行Γ总旧/新×各cellΓ新/旧；alpha>0与记录顺序定义保证该式，无graph依赖multinomialcoef。ESS4三链lgamma复算相同−161.9686682342。

I25-M12（L182–185）：伪计数alpha×同p0的candidatefamily marginal，q/r父状态编号已定；共同jointp0保证跨graph协同，而不是每图各自选uniformprior独立与ESS。

I25-M13（L193–198）：BMA对全图族以结构posterior加权within-graph参数posterior predictive；覆盖/近似/类先验数目限制在式后，不误用重复爬山频率。

I25-M14（L207–212）：addparent导致LLgain=n empiricalCMI且罚changeΔk/2logn；同data/完整freeCPT前提继承，空图12gain34.5038356，非固定α检验阈值。

I25-M15（L218–226）：DP空集0，枚举汇点i及其remainingparents、再最优残图；currentU无outgoingfromi所以无环。覆盖allDAG在可分scores/allowedparents空间，备表与subset指数代价另记。

I25-M16（L230–232）：cluster约束每nonemptyU至少有node父集避U，排directedcycles；binary z与每node恰选一已在公式前，指数约束和certification范围说明在后。

I25-M17（L236–246）：NOTEARS矩阵Y行records,Wsourcei→targetj，YW为线性predict；残差/λL1/h0三角色明示。h矩阵exp而Hadamardsquare确保非negativepaths，求法仍nonconvex，未声称因果唯一。

I25-M18（L248–251）：expB的m0trI=d被减去，m≥1闭walk迹正权累加；有cycle iff至少一tracepositive，gradient转置可得2W○exp(B)ᵀ，包含selfloop排除。

I25-M19（L264–268）：qold为当前graph/theta给Dobs的Z posterior；用于下一候选软count而不是其自身posterior，不随候选在比较中重算。

I25-M20（L270–276）：每record indicator候选nodefamilystate取E并加总；parentScope跟candidateG变而weight仍qold，observedcomponents固定，不丢未来家庭联合posterior。

I25-M21（L280–291）：Q expectationcompleteLL、F=Q+fixedH−pen；sameZspace+exactqold使观测penLL的common lowerbound在current触点，pen是否适用可由此看。

I25-M22（L293–300）：Lnext≥Fqold(next)≥Fqold(old)=Lold；第一来自bound、第二Q−penincrease、最后exactposterior，方向与每条件匹配，不是任意任换graph都monotone。

I25-M23（L306–309）：ElogΓ(alpha+N)一般不等logΓ(alpha+EN)；nonlinearity解释期望count替证据近似，constantN例外不影响“一般”限定。无罚MLcountlinear结论不能直接继承。

I25-M24（L325–332）：固定treeMLE单margproduct×pairratio；singlepositive避免divisionzero，pairzero允许pzero，leafsum normalization，无extraZ。任意tree相同familymargins未需causalorientation。

I25-M25（L338–343）：empMI自然log，0pair按0log0；formaltheorem以finite完整n≥1、positiveallstates/freeCPT/allsptrees定义候选，边权目标明确。

I25-M26（L350–353）：rootedtree joint=qrootΠconditional，每非root恰一parent，localtable约束independent，证明固定treeMLE时所有单parentconfig有正count。

I25-M27（L357–367）：平均MLELL=−Σsingleentropy+ΣtreeMI；由插入M24把marginalscope归组，样本平均不漏n。treeindependent常数使结构maxweight精确、params已经各自最优。

I25-M28（L376–383）：binaryuniformmarg下MI=log2−hbin(epsilon)，h自然log；三个epsilon不同直接导三权，边缘非uniform时此shortcut不可用而原MIformula仍可。

I25-M29（L396–399）：tree参数dimΣ(ri−1)+Σedges(ri−1)(rj−1)，来自rootedCPT重新归组且对根不敏感；constantstates时same dim，异r需BICweight改。

I25-M30（L408–411）：GaussianΣPD下offdiagK0 iffXiCI Xj给全部其余，限定i≠j由“零元素”/两变量邻接上下文；Kdiag>0不作CI判据。nonGaussian此语义不继承。

I25-M31（L415–422）：−logdetK+tr(ŜK)+λsumoffdiag形成稀疏precision；PD约束只给可行密度，未给minimum存在，I25-F02。λ0singularS无finiteopt，λpositivezero samplevariance亦无界。

I25-M32（L426–430）：条件mean mu_i−ΣKij/Kii(Xj−mu_j)，Kii>0；zero pattern匹配nodeconditionalregression，OR/AND与jointPDcompatibility在后。

I25-M33（L434–448）：K与Σ乘积确I，leadingminors2/3/4保证PD，Σ13=.25与K13=0例证marg/conditional不同；−K12/K11=.5，节点2两coeff=.5。

I25-M34（L455–459）：finitepositiveexpfeaturemodel A归一，dictionaryscopes/identifiablecoding先给；与下NLL对应，generalgraph不能只按pairfeature恢复高阶。

I25-M35（L463–467）：A−ΣθempEf+λL1为average NLL，modelgradientE[f]−empE[f]引推断成本；λ0finiteθ MLE可能只逼boundary，I25-F04，不把公式min读作总可取到。

I25-M36（L471–474）：Ising±1各状态field sign相反，所以logodds2ui；localfield/independentotherfixed已给，字面2倍与coding一致，支持logisticneighbor。

I25-M37（L478–482）：8个paritystates四+四−故normalizer8coshθ，θ≠0；sum1state得到pair1/4，thirdmomenttanhθ非零，positivejoint却notpaironlyindep解释。

I25-M38（L489–498）：Schur precision=KOO−KOH KHH⁻¹ KHO，jointΣPD保证blocksPD；Sconditionalprecision,LPSD/rank≤H，marginal ΣOOinv不能误用KOO直接submatrix。

I25-M39（L502–505）：3dimΣ=I+11ᵀ，inverseI−11ᵀ/4可乘验；offdiag−.25完整obsconditionalgraph但givenhiddenindepS=I，rankL1说明conditioning对象变。

I25-M40（L509–520）：min sparse/lowrank K=S−L PD、LPSD，S全entries罚/traceL PSD核norm/γpositive皆解释；λ0singularobservedS无finiteopt亦I25-F02。λ>0罚Sdiag故与M31existence边界不同，不宣称分解自动唯一。

I25-M41（L549–551）：LiNGAM Xj=ΣbjiXi+epsj，Browj/colsourcei在552另明确，recursiveacyclic→invertI−B；indnongaus/finitepositivevar/noconfounding给direction identification条件。

I25-M42（L562–568）：perfectinterventiontargetqproduct×nontargetoriginalCPT，knownI/indrandomq/othermechanismsfixed；parents仍代观测target值，fixeddo作为degenerateq，CI等价另需supportcoverage。

I25-M43（L585–590）：recordr只sum nontargetj原mechanismlogCPT，targetq已known或graphindependent可去constant；eachmechanism不同effective n，targetrecord仍fit its child，multi-environment共享定义不漏。

I25-M44（L644–648）：Delta=minnonedge minallpathf(I_f−I_e)，d≥3/uniquetree排empty/tie；最大树cyclecriterion每path边高于e，allerror<Delta/2维持strictorder，gap复算.0726544936。

I25-M45（L670–674）：bootstrap adjacencyfreq=indicatoravg overB；recordsIID抽nwithreplacement定义先给，direction/conditionaldenominator/CPDAGunknown/retune/stratify/block在后；此量不posteriorprob。

## 完整表、定理和数例

I25-T01（L73–85全表，关联U019–022）：读列名x1,x2,x3/次数及并排右半列；左4格36,9,1,4，右4格4,1,9,36，和100。三单点每状态50。二元pair12=(45,5;5,45)，23=(40,10;10,40)，13=(37,13;13,37)。条件2=0四格36,9,4,1，边缘45/5与40/10，2=1对称，所有格乘积成立。表注公平根独立翻转率.1/.2生成所示概率，未声称实际100次随机样本必恰等频率。表与后PC/BIC/Dir/tree/do的同一资料成立。

I25-T02（L599–614全表）：表头路线/关键条件信息/理想目标限制。PC行充分、无环、Markov忠实、oracle→CPDAG且可逆方向保留；GES行scoreequiv/decomposable/localconsistent+相应DAG→大样本CPDAG，未把一般greedy假称有保证；FCI行hidden/Markov/faithful/selection→PAG非fullhidden；LiNGAM行linearacyclic/indnonGaussian/noconfound→modelDAG，distribution shape条件保留；ANM行indadditive/nohidden/identifiable→uniqueDAG有exceptions，未全非线性自动；GIES行knowntargetperfect/nohidden/invariance/score→I-MECsearch不一般globalcert。六行均按info-assumptions-output，caption限定总体条件与actual3errors。PC/其余“无混杂”受I25-F05首次定义修正后使用，表本身输出一致。

I25-TH01（L336–372正式Chow–Liu定理与完整证明）：先固定n/状态域/positiveallsingles/freeCPT/allsptrees/zero convention；固定tree rootedtable MLE给marginals，叶sum归一；平均LL熵常数+edgeMI联合优化；Kruskal交换forestsubsetoptimal归纳具体证明。无假定全部pairpositive、无参数 tying/penalized objective、不把总体分布已为tree当定理条件。任一maxweighttie都ML，consistent unique tree另643设gap。未发现证明缺口。

I25-N01（L71–110 PC）：G²/α.05/df1critical3.841和给2CI0复算，骨架123与Sep13={2}；2在Sep故不collider，finite稀格只操作演示。I25-N02（L138 BIC）：空/链/完整参数3/5/7，LL−207.9441542/−151.8632577/−151.8632577，BIC−214.8519094/−163.3761832/−167.9813534，链最大且三链同类无因果唯一。
I25-N03（L166 BF）：赔率3×1/2=3/2，非把1.5当prob。I25-N04（L188–190 Dir/BDeu）：qi=2,ri=2,ESS4→cell1，row45/5→mean46/52与6/52，ML45/50与5/50；三链ordered-data logevidence由lgamma精确复算−161.9686682342。
I25-N05（L213 move）：100MI12−.5log100=34.5038356，Δk1符合add12；不作固定显著性阈值。I25-N06（L303 SEM）：00后Zweights .36/.01→36/37,1/37，sum1；currentchain假设明示、candidatefamily软count而非硬fill。
I25-N07（L375–395 tree）：MI12=.3680642072,MI23=.1927447570,MI13=.1200902634，retain12/23sum.5608089642；p000=.36,avgLL−1.5186325775；同表 exacttree而一般bestapprox。I25-N08（L433–449 Gauss）：KS=I及PD主子式/conditionalcoeff已复算见M33。
I25-N09（L477–483 parity）：符号列四正四负归一，任θ≠0pairMI0但thirdtanhθ≠0；θ=.7数值sum1，third .6043677771等tanh(.7)，该数为复核自算非新增正文。I25-N10（L501–506 latentGaussian）：std independent→diag2/offdiag1，K=I−11ᵀ/4，conditionalS=I与margdense对象分开。
I25-N11（L559–580 do）：同三表示fit table；do2=1链root1=.5/child3=.8；叉child1=.9/child3=.8；reverseupstream3=.5/child1=.9。条件2=1的三表示都给.9/.8；互换do2=0也可区分，给定总体/覆盖两值范围符合判据。I25-N12（L643–649 gap）：MI23−MI13=.0726544936，display .072654舍入正确，all-estimate errors<gap/2使两权差保正，不宣称tie时图一致。

I25-FIG01/02/03（图注U008/U084/U128）：实际只读parent current figure.png；equivalence三directed链/叉无collision、底CPDAGundirected；Chow–Liu三边权及两solid/一dashed对应数例；intervention蓝/黄/红bands、rightprobbox .5/.8,.9/.8,.9/.5，虚线切入2的12或32，叉无cut。右框边/连接箭头同色（middlegreen），未按yellow band同色解释；caption颜色主体可读为框箭头一致。图元数/箭头语义符合正文；不在本轮检查页面布局。

本轮没有正式algorithm环境；PC/GES/DP/IP/NOTEARS/SEM/Kruskal/GIES/bootstrap的全部流程句及约束已逐W/M覆盖，未把“没有algorithm环境”当免审算法说明。
