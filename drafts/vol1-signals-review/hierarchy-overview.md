# 信号章标题层级总览

以下标题来自当前四份分稿，用于快速检视subsection以下的分组；编号仅作设计定位，正文尚未实施。未列入口、共同收束等无标题自然段。

来源：[对象与表示、信号比较](outline-01-representation-comparison.md)、[基本运算与映射](outline-02-operations-mappings.md)、[卷积](outline-03-convolution.md)、[采样、多尺度与量化](outline-04-sampling-multiscale-quantization.md)。

## 1 section：信号的对象与表示

### 1.1 subsection：信号对象与边界

分组依据：按信号对象必须先固定的索引、取值、周期与记录边界分组。

- 1.1.1 subsubsection：索引集合与物理位置
  - paragraph：连续、离散与有限索引
  - paragraph：采样间隔与物理单位
- 1.1.2 subsubsection：信号的取值
  - paragraph：实值与复值
  - paragraph：标量与多通道取值
- 1.1.3 subsubsection：信号的周期性
  - paragraph：周期与基本周期
  - paragraph：复指数周期与多通道共同周期
- 1.1.4 subsubsection：支撑与边界约定
  - paragraph：支撑与观测范围
  - paragraph：零、周期与反射延拓
  - paragraph：输出索引与裁剪

### 1.2 subsection：位置分解与截断

分组依据：沿位置坐标的建立与使用展开，依次说明单位脉冲、脉冲展开及无限记录的截断收敛。

- paragraph：单位脉冲与移位
- paragraph：脉冲展开
- paragraph：位置截断与范数收敛

### 1.3 subsection：全局傅里叶表示

分组依据：按有限记录、周期信号、整轴离散序列与整轴连续信号四类对象分别建立傅里叶表示。

- 1.3.1 subsubsection：有限记录的DFT
  - paragraph：离散傅里叶变换与重构
  - paragraph：Parseval关系
  - paragraph：幅相、平移与实值对称
  - paragraph：逐轴DFT的计算
- 1.3.2 subsubsection：周期信号的傅里叶级数
  - paragraph：傅里叶系数与谐波展开
  - paragraph：均方与逐点重构
  - paragraph：Parseval关系与截断误差
- 1.3.3 subsubsection：整轴离散序列的DTFT
  - paragraph：DTFT与频谱周期
  - paragraph：逆变换与平方量关系
  - paragraph：DTFT与DFT的联系
- 1.3.4 subsubsection：整轴连续信号的傅里叶变换
  - paragraph：傅里叶变换与逆变换
  - paragraph：L2延拓与Plancherel关系
  - paragraph：平移、尺度与仿射坐标变换
  - paragraph：时域支撑与频域支撑

### 1.4 subsection：频率表示的选择与调整

分组依据：按改变记录边界与读取局部片段两种表示需求分组，各自解释坐标、重构及读数限制。

- 1.4.1 subsubsection：反射边界的余弦表示
  - paragraph：镜像延拓与DCT
  - paragraph：正交重构与截断误差
  - paragraph：整数近似与逆变换尺度
- 1.4.2 subsubsection：局部片段的时频读数
  - paragraph：STFT与帧位置
  - paragraph：短时谱的幅相与谱图
  - paragraph：窗口频谱与频谱泄漏
  - paragraph：窗长与时频分辨
  - paragraph：频带汇总与梅尔特征

### 1.5 subsection：多项式坐标与恢复

分组依据：按位置系数、点值与多项式余数三种坐标组织，并在各坐标内部建立恢复条件。

- 1.5.1 subsubsection：位置系数表示
- 1.5.2 subsubsection：点值表示与插值恢复
  - paragraph：插值唯一性与Lagrange公式
  - paragraph：次数约束与数值稳定性
- 1.5.3 subsubsection：余数表示与模分解恢复
  - paragraph：带余除法
  - paragraph：互素与Bézout恒等式
  - paragraph：中国剩余定理与重构
  - paragraph：模边界与次数约束

## 2 section：信号的比较

### 2.1 subsection：信号大小的度量

分组依据：按峰值、绝对幅值累计与平方范数三种大小指标分组，分别明确其适用对象。

- paragraph：峰值与本质上界
- paragraph：绝对幅值的累计
- paragraph：平方范数

### 2.2 subsection：信号差异与方向相似性

分组依据：围绕两信号的比较，区分内积方向、距离误差与归一化相似性。

- paragraph：内积与正交
- paragraph：距离与逐点误差
- paragraph：归一化内积与相对相位

### 2.3 subsection：累计能量与平均功率

分组依据：按整轴累计能量与长期平均功率两个不同指标分组，分别说明计算与存在条件。

- 2.3.1 subsubsection：信号能量
  - paragraph：整轴能量与窗口能量
  - paragraph：能量的频域计算
- 2.3.2 subsubsection：平均功率
  - paragraph：平均功率的定义与存在性
  - paragraph：周期信号的平均功率
  - paragraph：有限能量与零平均功率

## 3 section：信号的基本运算

### 3.1 subsection：信号的位置变换

分组依据：按平移、反转与时间缩放三种位置变换分组，数组约定及大小变化放在对应变换内部。

- 3.1.1 subsubsection：平移与延迟
  - paragraph：平移的定义与计算
  - paragraph：能量与窗口裁剪
- 3.1.2 subsubsection：时间反转与数组反序
  - paragraph：反转与反序
  - paragraph：取负与共轭
- 3.1.3 subsubsection：时间缩放
  - paragraph：连续时间缩放
  - paragraph：能量与平均功率

### 3.2 subsection：信号的幅值运算

分组依据：按幅值叠加、同位置相乘与通道混合三种作用方式分组，计算和性质随对应运算说明。

- paragraph：幅值缩放与叠加
- paragraph：逐点乘法与加窗
- paragraph：多通道混合

### 3.3 subsection：信号的差分

分组依据：围绕差分这一运算，先建立算子与计算，再解释其作为导数近似时的误差和条件。

- paragraph：差分算子与计算
- paragraph：导数近似与误差

### 3.4 subsection：信号的相关

分组依据：围绕滑动内积的不同读数，说明互相关、输出范围、归一化与自相关。

- paragraph：互相关
- paragraph：完整与有效相关
- paragraph：归一化相关
- paragraph：自相关

## 4 section：信号的映射

### 4.1 subsection：输入输出映射的界定

分组依据：先界定输入输出映射，再单独说明初值如何形成自由响应及其与输入响应的关系。

- paragraph：信号映射
- paragraph：初值与自由响应

### 4.2 subsection：映射的性质与检验

分组依据：按线性、时不变性、记忆与因果性四个可分别检验的性质组织。

- paragraph：线性
- paragraph：时不变性
- paragraph：记忆
- paragraph：因果性

### 4.3 subsection：典型映射的结构与计算

分组依据：按线性核、输入依赖的非线性规则与集合或灰度形态规则三类映射结构分组。

- 4.3.1 subsubsection：线性核映射
  - paragraph：有限维响应核
  - paragraph：因果核
  - paragraph：时变核
  - paragraph：固定滞后核
- 4.3.2 subsubsection：输入依赖的非线性映射
  - paragraph：逐点门控
  - paragraph：输入依赖核与因果性
- 4.3.3 subsubsection：集合与灰度的形态映射
  - paragraph：膨胀与腐蚀
  - paragraph：膨胀与腐蚀的性质
  - paragraph：开闭运算
  - paragraph：灰度膨胀与腐蚀

### 4.4 subsection：给定输入附近的局部线性化

分组依据：围绕有限维可微映射的一阶近似，先建立导数计算，再说明基点依赖和可微边界。

- paragraph：导数映射与一阶近似
- paragraph：基点依赖与可微条件

## 5 section：信号的卷积

### 5.1 subsection：卷积的定义与计算

分组依据：按离散与连续位置两种运算对象分组，记录边界、循环、多维网格和通道均在离散对象内部展开。

- 5.1.1 subsubsection：离散卷积
  - paragraph：离散卷积的定义
  - paragraph：离散卷积的直接计算
  - paragraph：有限记录的边界与输出
  - paragraph：循环卷积
  - paragraph：多维离散卷积
  - paragraph：多通道卷积
- 5.1.2 subsubsection：连续卷积
  - paragraph：连续卷积的定义与计算
  - paragraph：连续单位脉冲

### 5.2 subsection：卷积的性质与成立条件

分组依据：围绕卷积可组合、影响范围、存在性、幅值控制和无限输入表示等性质问题直接组织段落。

- paragraph：卷积的代数性质
- paragraph：串并联与矩阵核
- paragraph：支撑与因果性
- paragraph：绝对收敛与可积性
- paragraph：有界输入的幅值界
- paragraph：ℓ¹输入的卷积表示

### 5.3 subsection：卷积的矩阵与频域表示

分组依据：按矩阵与频域两种表示分组，可逆性、整轴频率响应和加窗关系在频域表示内展开。

- 5.3.1 subsubsection：卷积的矩阵表示
- 5.3.2 subsubsection：卷积的频域表示
  - paragraph：循环卷积定理与DFT对角化
  - paragraph：循环卷积的可逆性与反演敏感性
  - paragraph：频率响应与整轴卷积定理
  - paragraph：逐点乘法的DFT关系

### 5.4 subsection：卷积滤波与模板匹配

分组依据：按平滑、变化检测与模板匹配三种处理用途分组，再用具体滤波核说明计算和限制。

- 5.4.1 subsubsection：平滑滤波
  - paragraph：均值滤波
  - paragraph：指数平滑
  - paragraph：高斯滤波
  - paragraph：硬截止低通滤波
- 5.4.2 subsubsection：差分与导数滤波
  - paragraph：差分滤波
  - paragraph：Sobel滤波
  - paragraph：高斯导数滤波
- 5.4.3 subsubsection：模板匹配的卷积实现

### 5.5 subsection：卷积的快速计算

分组依据：按矩阵乘法、FFT、多项式插值、余数分解与核分离五条计算路线分组，末尾集中比较算法并说明精度条件。

- paragraph：计算目标与直接算法
- paragraph：多项式乘法与卷积
- 5.5.1 subsubsection：基于矩阵乘法的计算
  - paragraph：窗口矩阵的构造与计算
  - paragraph：矩阵化的计算与存储
  - paragraph：Strassen矩阵乘法
- 5.5.2 subsubsection：基于FFT的计算
  - paragraph：FFT的递归分解
  - paragraph：FFT卷积的计算
  - paragraph：分块FFT卷积
- 5.5.3 subsubsection：基于多项式插值的计算
  - paragraph：求值与插值计算
  - paragraph：短卷积的插值算法
  - paragraph：Toom–Cook递归算法与代价
- 5.5.4 subsubsection：基于余数分解的计算
  - paragraph：小块滤波的计算目标
  - paragraph：多项式余数重构
  - paragraph：F(2,3)的推导与计算
  - paragraph：二维F(2,3)
- 5.5.5 subsubsection：基于核分离的计算
  - paragraph：可分离卷积的定义与计算
  - paragraph：可分离卷积的计算代价
  - paragraph：低秩卷积与近似误差
- 5.5.6 subsubsection：算法比较与精度条件
  - paragraph：计算路线的比较
  - paragraph：有限域与数论变换
  - paragraph：整数卷积的恢复

## 6 section：信号的采样与恢复

### 6.1 subsection：采样的定义与计算

分组依据：按点值读取、区域平均与已有序列抽取三种采样规则分组。

- 6.1.1 subsubsection：点值采样
  - paragraph：采样时刻与索引
  - paragraph：规则采样格
- 6.1.2 subsubsection：区域平均采样
  - paragraph：面积与曝光读数
  - paragraph：盒形平均的频率响应
- 6.1.3 subsubsection：离散抽取

### 6.2 subsection：采样的混叠与信息损失

分组依据：按连续对象的均匀采样与离散序列的抽取两种信息丢失机制分组。

- 6.2.1 subsubsection：均匀采样的混叠
  - paragraph：一维频率等价
  - paragraph：多维采样格的频率等价
  - paragraph：运动与帧采样
- 6.2.2 subsubsection：离散抽取的混叠

### 6.3 subsection：采样恢复的条件与方法

分组依据：沿带限类的恢复论证组织，依次建立点值、频谱复制、唯一性、重构及有限观测边界。

- paragraph：带限信号与规范点值
- paragraph：采样频谱的周期复制
- paragraph：无混叠条件与欠采样歧义
- paragraph：sinc重构
- paragraph：恢复条件与有限观测
- paragraph：多维网格重构

### 6.4 subsection：采样率转换与实现误差

分组依据：按降采样与升采样两类采样率转换分组，滤波、抽取或插零以及实现误差放在对应转换内部。

- 6.4.1 subsubsection：降采样的预滤波与抽取
  - paragraph：抗混叠频带与抽取规则
  - paragraph：均值预滤波与混叠残留
  - paragraph：池化与抽取相位
  - paragraph：预滤波的实现误差
- 6.4.2 subsubsection：升采样的插零与插值
  - paragraph：插零与频谱镜像
  - paragraph：插值核与计算步骤
  - paragraph：插值的保真条件

## 7 section：信号的多尺度分解与重建

### 7.1 subsection：平均与细节的正交分解

分组依据：围绕Haar正交分解组织平均与细节、逆变换、数例、多层关系及二维子带。

- paragraph：Haar平均与细节
- paragraph：逆变换与正交性
- paragraph：Haar分解与重构算例
- paragraph：多层分解与正交细节
- paragraph：二维Haar子带

### 7.2 subsection：双通道滤波的完全重建

分组依据：围绕双通道分析与合成，依次说明计算规则、混叠分解、完全重建条件及有限边界。

- paragraph：分析与合成规则
- paragraph：合成输出的两项分解
- paragraph：完全重建条件
- paragraph：Haar型滤波器
- paragraph：有限数组的边界与延迟

### 7.3 subsection：粗层预测与残差重建

分组依据：围绕粗层预测与残差这一重建结构，分别说明对象、逐层算法和存储代价。

- paragraph：粗层与残差
- paragraph：分析与逐层重建
- paragraph：多层存储量

## 8 section：信号的量化与编码

### 8.1 subsection：量化规则与幅度误差

分组依据：围绕幅值量化规则，先说明均匀量化与饱和，再建立非饱和区间内的误差界。

- paragraph：均匀量化与饱和
- paragraph：非饱和量化的误差界

### 8.2 subsection：量化后的重建与误差传播

分组依据：按正交系数量化与预测差值闭环编码两种重建结构分组，分别追踪误差的作用位置。

- 8.2.1 subsubsection：正交系数量化
- 8.2.2 subsubsection：预测差值的闭环编码
  - paragraph：DPCM编解码规则
  - paragraph：闭环重建误差
  - paragraph：历史失配的误差传播
