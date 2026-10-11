# 29 W 特殊单元 r1

固定原稿 `5cee06782bf5cd1ccde8531eeae1785656045e2250a23c954af55da4430597e4`，先完成本文件全部单元，再核作者记录及后续增量。正文 437 行政句地址已经真实逐句读完；定位核对返回 437/437，无缺漏。下表的数学判断手工写入，不由计数脚本生成。原稿 56 个显示数学环境、289 个行内数学片段、5 图注、1 完整表、1 完整算法、3 示例。289 行内片段已在所在句的对象/形状/条件/数值审读中核查，`inline-addresses.json` 只定位，不代表通过依据；有意义的作用与推导见 W 各句和下列显示式。

## 显示公式 EQ01–EQ56（按原稿顺序）

| 单元/行 | 对象与白话意思 | 实际核对依据 |
|---|---|---|
| EQ01 L14 | 平均观测负 log 密度 | 负号决定最小化方向；θ仅索引模型，1/n是样本平均。可为无穷值的极端模型不影响目标定义，本文未承诺任意θ有限。 |
| EQ02 L36 | VAE prior×conditional joint，再 integrate z 得 observation marginal | p(z)、p(x|z)各归一化且非负，Tonelli 推 p(x)积分1；latent维度k与obs维度d未混。 |
| EQ03 L49 | positive isotropic Gaussian decoder | mean g:Rk→Rd，covτ²Id，τ>0；完整采样另需 independent η，不仅输出mean。 |
| EQ04 L59 | linear Gaussian observation distribution | basecovIk 经W得WWT，加independentnoiseτ²Id；meanb，shape d×d。 |
| EQ05 L66 | linear latent posterior | posteriorprecision I+τ⁻²WTW positive definite；Σ inverse、m=τ⁻²ΣWT(x−b)正确，即使W缺秩仍有效。 |
| EQ06 L83 | x=2 的 posterior completing-square | z²+(2−2z)²=5(z−.8)²+.8；非关z常数吸收比例，variance .2而不是precision .2。 |
| EQ07 L95 | VAE ELBO | Eq logcond−KL(q||prior)≤logp，q是approxposterior而非generativemarginal；φ/θroles紧后说明。 |
| EQ08 L117 | diagonal Gaussian qφ | eachs>0，diag s²k×k；networklogvariance经exp得variance，sampling需stds。 |
| EQ09 L125 | diagonal q to standard prior KL | .5sum(m²+s²−1−logs²)，logratio方向q||p正确，m/sdependx省略已解释。 |
| EQ10 L145 | Gaussian decoder NLL | norm²/(2τ²)+d/2log2πτ²；τfixed时secondtermconstant，learnedτ须保留两项。 |
| EQ11 L153 | binary conditional-independent NLL | Bernoulli productlog给coordinateBCE；x∈{0,1}，不将fractionalcontinuous values当此probabilitymass。 |
| EQ12 L162 | posterior-tight ELBO toycomponents | E residual²=.16+.8=.96；Elogcond=−.9189385−.48，KL=.72471896，subtract得−2.12365749。公式本身所有行正确。 |
| EQ13 L175 | total current inference gap split | 插入/减去sup_Q L，固定θ且qφ∈Q；两差距非负，second含optimization，不全部叫纯摊销。 |
| EQ14 L201 | aggregated encoder posterior | pdata 下对normalized qφ mixture；可作normalization integral，与prior mismatch对象清楚。 |
| EQ15 L208 | per-datum KL information decomposition | pdata qφ joint，finite KL后add/sublogqagg gives Iq+KL(qagg||p)；不是generatorjoint的mutual information。 |
| EQ16 L232 | Flow density change | p0(inversex)|detinverseJ|；logform subtractforwardlogdet at z；C1diffeomorphism/nonzeroJ sufficient。 |
| EQ17 L246 | finite composite Flow likelihood | hℓ=fℓ(hℓ−1)，logdet chainproduct→sum；evaluation points hℓ−1与mappingorientation一致。 |
| EQ18 L258 | √5 scaling density toy | z²=.8，base log−.5log2π−.4，minuslog√5 yields−.5log10π−.4；同obsdensity不同latentuncertainty。 |
| EQ19 L274 | affine coupling | xA=zA，xB=zB exp a(zA)+b(zA)，positivecomponentexp；inverse recoverA then undoB。 |
| EQ20 L286 | coupling Jacobian and logdet | upper-rightzero/lower-leftcrossderivative，diagB expa；det productexpa,logsum correctdimensions。 |
| EQ21 L311 | MAF dependence on x-prefix | prefixx<j isknownforfullobservation eval，可maskedparallel；generation需要orderedprefix。 |
| EQ22 L320 | CNF progression ODE | u0→1 base→obs，spatialC1/uniqueness/fullintervalbothdirections supportinvertibleflow；not trainingtime。 |
| EQ23 L328 | instantaneous and integral log density | total derivative alongtrajectory−divv，integral base minusdiv; localpositivevolume impliesdensitydecrease。 |
| EQ24 L353 | conditional posterior Flow density | fixedx transform u→z，对u求Jacobian；logq0−logdet forward，no marginal p(x) claim。 |
| EQ25 L377 | DDPM fixed forward path | βt∈(0,1)，α=1−β，barαproduct/barα0=1；eachnormalizedGaussianconditional yieldsnormalizedqpath。 |
| EQ26 L391 | known-x0 forward marginal and sampling | mean√barα x0、variance1−barα，x=mean+sqrtvariance ε；ε ismarginalcomposite not multi-tpathnoise。 |
| EQ27 L406 | known-x0 terminal KL | meanenergybarα||x0||²+trace d(1−barα)−d−dlog(1−barα); simplifiesprintedform。finite2ndmomentdataavg→0。 |
| EQ28 L420 | N(0,5) noised marginal | variance5barα+1−barα=1+4barα; derivative later score−x/v，consistent। |
| EQ29 L427 | normalized reverse latent path and observation | priorTΠp(prev|current)，integratex1:T；generationdescendingt despite productnotationascendingindex。 |
| EQ30 L463 | path negative ELBO | logp0≥Bdiff，Jdiff=E_q log(qpath/pjoint)=-B；joint includesx0 whileqconditionsx0。 |
| EQ31 L478 | known-x0 Bayes reversal | denominatorqprev|x0 andnumeratorqt|x0；Markov qcurrent|prev plusfixedx0 allowidentity，t≥2 avoidszero-widthx0prior。 |
| EQ32 L485 | local DDPM objective decomposition | terminal KL+sumt2:T E_qt KL(known-x0target||model)−E_q1logdecode；decoder countedonce,expectationcorrectcurrentdensity。 |
| EQ33 L505 | posterior precision algebra | α/β+1/(1−barprev) denominatorβ(1−barprev)，numeratorα(1−barprev)+β=1−bart。 |
| EQ34 L512 | Gaussian known-x0 reverse posterior | βtilde=β(1−barprev)/(1−bart)，μtilde βtilde timeslinear coefficient；weights√barprevβ/noise and√α(1−barprev)/noise正确。 |
| EQ35 L531 | target Gaussian vs model Gaussian KL | mean-error /2σ² +d/2[βtilde/σ²−1+logσ²/βtilde]；covariance partpositive andzeroifσ²=βtilde。 |
| EQ36 L546 | posterior mean via composite noise | replace x0 by(xt−√noiseε)/√bart gives(xt−βε/√noise)/√α；usesknownsamplepairnotgenaccessx0。 |
| EQ37 L553 | learned mean parameterization | replaceε withεθ，coefficientβ/(√α√noise)；validany t≥1 withnoisepositive。 |
| EQ38 L562 | weighted intermediate denoising target | subtractmeansxtcancels，normcoefβ²/[α(1−bart)] and2σ² yieldswt；Ct/weight outsideE validtime-onlypresetσt，notgeneralstate-dependentcase（R01澄清）。 |
| EQ39 L579 | one-step mean-error check | .25²/(.75×.4)×.3²=.01875；divide .5 gives.0375，matchesw5/12times.09。 |
| EQ40 L586 | uniformly sampled simple loss | ExpecttUniform1:T,data,standardεindependent；sameunweightedregression notsameboundvalue，中间sum校正T−1另讲。 |
| EQ41 L600 | conditional Gaussian score | derivativewrtxt=−(xt−√bart x0)/(1−bart)=−ε/√noise；denominatorvariancevsstd分别正确。 |
| EQ42 L607 | marginal score conditional averaging | swap derivative/integral andqt>0，posteriorx0weightedcondscore; equals−Eε|xt/√noise，not actualε。 |
| EQ43 L619 | DSM orthogonal error split | sθ(xt) measurable，residuala−E[a|xt] conditionalmean0 killscross term；finiteL2，lasttermθ-independent。 |
| EQ44 L628 | reverse mean from marginal score | μθ=(xt+βsθ)/√α；exactscoregivestrueconditionalmeanviaaveraging μtilde，doesnotfullkernelGaussian。 |
| EQ45 L667 | time-isotropic forward SDE | b(X,t)dt+g(t)dW，initialpdata；regularitynonexplosionwritten，noiseonlytime是laterformula条件。 |
| EQ46 L683 | decreasing-t reverse SDE | drift b−g²score乘dt<0，reverse Brownian cov|dt|I；increasing-notation不能照抄同minusdrift。 |
| EQ47 L694 | increasing-u reverse SDE | u=Tc−t gives−b+g²score，positiveBrownian Bu；coefficients timeTc−u，all signsconsistent。 |
| EQ48 L707 | Euler--Maruyama sampling step | Δu>0，−bΔu+g²sθΔu+g√Δuξ，ξfreshindependent；discretized fieldnotexactrecoveryclaim。 |
| EQ49 L718 | probability-flow velocity | v*=b−½g²s*，ODE; halfcoefficientfromFokker--Planckrewrite，与inverseSDEfullcoefficientdifferent。 |
| EQ50 L729 | forward Fokker--Planck | isotropica=g²I givesdiffusion .5g²Δq；b divergencefullincludingpositiondependence。 |
| EQ51 L734 | probability-flow continuity | qscore=∇q，g spatialconstant，−div[(b−.5g²score)q]; samePDEplusboundary/uniquenessyieldonlytime-marginalequivalence。 |
| EQ52 L741 | learned ODE model log density | logp0=logpTc(endpoint)+∫0^Tc divvθ, evalfromx0，generationreverse; bidirectionalC1flow andterminaldensityconditions。 |
| EQ53 L757 | linear-field ODE example | endpoint e^a x0,divintegrala; resultnormalvariancee^-2a，a=−.5log5gives5；fieldindependentlyspecifiednotVPexactfield。 |
| EQ54 L840 | hierarchical VAE ELBO | numeratorp(z2)pθ(z1|z2)pθ(x|z1)，denominatorq(z1|x)q(z2|z1,x); exactjoint/approxjoint ratio，layeredsamplingestimate。 |
| EQ55 L855 | probabilistic latent diffusion observation density | normalizeddecoder andnormalizeddiffusionlatentprior define∫joint; lossymean-decoderalone differentprobabilitysemantics。 |
| EQ56 L867 | implicit pushforward probability | integrateindicatorpreimageagainstbase，Bmeasurable；legalprobabilitywithoutdensityoruniqueinverse，setsupportsF01必要性纠正。 |

## 五图注

- FIG01/P022/L109：标题、三句 caption、实线先验/条件生成与虚线 q 推断均按不同程序解释；ELBO 不是图中额外随机变量。固定宽112mm/图路径不修改。
- FIG02/P026/L137：四句 caption，m/s/ε 公式、负 ELBO 的优化方向、无条件 prior 及鸟为插画全部读；conditionmean图像并未替代随机 decoder。宽135.805mm冻结。
- FIG03/P053/L301：三句 caption，A preserved→subnet→B affine，lowertriangular volume与先A再B inverse，相同计算机制；宽112mm冻结。
- FIG04/P073/L441：四句 caption，fixed forward、learned reverse、scaleindices、独立抽两路径和terminalmisfit；不把图当true reverse trajectory复现。宽112mm冻结。
- FIG05/P076/L452：三句 caption，left→right forward/right→left reverse、freshterminalnoise、flower插画role；noise尺度不是时间顺序。宽139.534mm冻结。

本遍只核 caption 与概率机制，不宣称重新检查本轮像素或 PDF 排版；source图已先前逐节点审查，父代理另做终版页检查。

## TAB01/P119/L789 全表（不只图注）

- 表头四格：机制；完整观测似然；潜变量与条件查询；典型采样成本/限制。不是将不同model同一个“效果”数值排序。
- 自回归行：模型格为基线；fullnormalizedconditionproduct可exactevaluate；任意missingprefix不保证easymarginal；coordinateorderedancestral、ordercost。每项与P007同条件。
- VAE行：名称；ELBO training并非reportedmarginalexact；encoderapproxposterior；latentdraw+conditionaldecode，conditionalchoice影响cost。未把qforwardcost视generatoronlycost。
- 离散层Flow行：明确finite-layers；inverseandJacobian可行才directdensity；fullxuniquez而partialmarginal仍积分；layeredmap/autoregressive双向cost。未套CNFnumericalintegration“精确无误差”。
- DDPM行：pathELBO可estimate，simpleloss不是likelihood；forwardfixedpath是variationaldistribution而非trueposterior；T randomtransitions、terminal与Gaussianfamilyerrors。四格概率对象一致。
- 分数ODE行：divergence integraldefineownpODE；inverseencoding不是stochasticpathposterior；NFE/solverprecision。近似score下未把其density写成SDEdensity。
- 受约束PC行：normalizedexactdensity/mass；marginal/conditional能力有graphconditions；structuredsample但representationpossiblylarge。所有成本限定givenstructure。
- Caption三句：query/samplecost；math“精确”与float误差区分、continuousflow和scoreODE solver+traceextra；PC smooth/decomposable/normalized条件继承。6行×4格及表头/表注全部实际核过。

## ALG01/P093/L639 全算法

- 名称「固定方差DDPM的学习与祖先采样」：对象是离散normalized逆chain，训练target是simpleloss，不是continuousreverseSDEsolver。
- Require：continuousdataset/fixedβ/positiveσ²for1:T；β range由precedingforwarddefinition继承，positiveσ1 decoder特别重要。
- Ensure：噪声网络+该模型samples；未宣称learned truep_data或posteriorgroundtruth。
- 初始化θ并precomputeα/barα：sumproductindex与barα0=1可用，fixedschedule不作learnedgrad。
- 训练loop：每个batch至stop，budget/validation为本地knownstoppingcontext；notunboundedconvergenceguarantee。
- 每obs抽uniformt1:T与standardε：samplingvariablesindependent；sampledt改变learningbatch噪声尺度，不共享一个t所有数据必需。
- 按closedmarginalxt：只构造one scale不simulatepreviouschain，costO(Cnet+d)有依据。
- 用simpleloss更新θ：all t noise回归，无πimportance或wt，名称/随后说明明确不是严格ELBO。
- End训练loop：输出learnednetwork，停止后进入separategeneration，无datax0作为input。
- 生成xT standardnormal：终端prior是modelchosen，真实qtterminalmatch需training schedule另评。
- reverse loop t=T…2：T−1非boundarysteps，range避免t1βtilde0误用。
- network→μθ：inputsxt,t，formulaεparam中noisvariancepositive，不accessunknownx0。
- freshξt标准normal：independentstepinnovation，xprev=μθ+σtξt，使用stdσt而非varianceσt²。
- Endreverse loop：状态剩x1，notalreadyx0；single-stateMarkovmemoryclaimconsistent。
- 从pθ(x0|x1)抽x0并return：precedingP092definesmeanεnetworkandpositiveσ1，完整conditionalGaussian sample，不任意输出μθ冒充同law。
- 随后P094：strictvariant训练replaceweightedmiddle+decode；可展示末mean，但为differentoutput，不修改printedancestoralgorithm。

## 三示例及跨式数值

- EX01/P018：variance5，posteriorprecision5、mean.8、variance.2；noise导致manylatentpossible，Flow对比限定fullx。
- EX02/P047：scaling√5，inverse2/√5，density−2.12366；同target而postpointmassvsnormal不同，latentjointmechanism不identified。
- EX03/P084：两β参数=.2/.25，bar=.8/.6，βtilde2=.125，σ²=.25，wt5/12，noiseerr.3→mean².01875→meanKL.0375，Ct.09657→fullKL.13407；toy只algebra不是qualitybenchmark。
- P029 后验ELBO .96/Elog/KL三terms，qprior使residual8/KL0→−4.91894；带符号减KL对结果一致。
- P071 terminalmarginals KL atvariance2=.153426；variance1.04=.000389643；conditionalavgKL另term不能替代。
- P106 ODE linearfield result N(0,e^-2a) hasnormalizer+a，a=-.5log5恢N05；divergencesign实验为解析calculation而非numericbenchmark。

## 原稿本遍结论

已完整覆盖正文、标题和特殊单元，行政核对仅保障地址无漏、不代替判断。IND29-F01 待实际新稿连续上下文复核关闭；R01/R02 为范围/端点澄清建议。C/P/W 及全部公式判断绑定原 5cee…稿，不能改写为绑定尚未读的新稿。本轮无编译、无 PDF 重绘、无源码修改。
