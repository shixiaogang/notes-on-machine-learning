# 强化学习具身设定插图记录

- 生成日期：2026-10-04。
- 文件：`rl-overview-embodied-setting.png`。
- 生成服务：AI Horde公开分布式图像生成接口。
- 模型：`AAM XL`；服务未返回工作节点所用检查点的额外版本哈希。
- 参数：1024×704，seed 461，28步，CFG 7，`k_dpmpp_2m`，单张输出。
- 最终处理：从原图左上偏移$(230,230)$处裁取620×413像素区域，转为RGB PNG，并写入141 dpi元数据；未重绘、修补、上采样或添加画面内容。
- SHA-256：`a38b3a20e3f1e92978ee3f9d09953e7d4aae34a6a1dd568c8a33ec9d6a9b8fd6`。
- LaTeX叠加：`rl-overview-embodied-loop.tex`加入智能体、环境、动作、奖励与下一状态标签及箭头。
- 性质：原创教学概念图，不是实验图、观测照片、精确动力学模型或传感器结构图。

## 提示词

> flat vector editorial textbook illustration, clean isometric warehouse navigation scene on warm off-white paper, one small teal autonomous mobile robot with two visible wheels and a round camera sensor in the lower left, one amber cardboard box obstacle in the center, one amber charging dock goal in the upper right, two low slate-blue warehouse shelves framing a wide clear aisle, robot facing toward the open route around the obstacle, dark navy outlines, muted teal and slate blue, warm amber accents, pale gray floor, simple geometric shapes, subtle paper texture, generous empty space at top and bottom for later labels, restrained scientific educational illustration, exactly one robot, exactly one obstacle, exactly one goal

负向提示词：

> text, letters, words, numerals, formula, arrows, labels, logo, watermark, people, additional robot, duplicate robot, photorealistic, photograph, glossy 3d render, dramatic lighting, shadows, gradients, clutter, malformed wheels, collision

## 筛选与边界

生成原图的中央区域有一个移动机器人和一个明确的停靠区，配色与全书概念插图一致；画面外侧另有两个重复设备，不满足单一智能体要求，故采用固定裁剪排除。裁剪后的画面没有文字、伪标签、品牌、水印或可被误认为实验数据的数值。

模型没有可靠地产生提示词中的独立货箱障碍，最终图注和正文因此不声称图内精确展示货箱。插图只承担智能体位于环境中并通过动作改变后续状态的直观说明；精确交互方向由LaTeX箭头表达。
