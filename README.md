# Ariadne

面向2026年 TI 杯赛区赛 E 题《拼图装置》的 monorepo。目前包含资料与项目级 skills，尚无设备控制程序。

题目要求用视觉和机械机构把A4纸上半区的碎片搬到下半区拼成矩形，覆盖固定四片、未知白片与扑克牌碎片；写字机式平台是候选实现。

## 从这里开始

1. [题目与约束](.agents/skills/nuedc-2026-e/references/requirements.md)
2. [评分与测评](.agents/skills/nuedc-2026-e/references/scoring.md)
3. [参考项目](.agents/skills/puzzle-integration/references/references.md)
4. [来源索引与证据边界](docs/sources.md)

## 技能索引

- [nuedc-2026-e](.agents/skills/nuedc-2026-e/SKILL.md)：解释 2026 年 E 题拼图装置，核对任务、尺寸、评分和测评规则。
- [puzzle-vision](.agents/skills/puzzle-vision/SKILL.md)：开发或排查拼图碎片分割、轮廓提取和姿态识别。
- [puzzle-calibration](.agents/skills/puzzle-calibration/SKILL.md)：标定相机、纸面和运动平台之间的坐标映射并评估误差。
- [puzzle-solving](.agents/skills/puzzle-solving/SKILL.md)：设计固定或未知多边形碎片的矩形拼接与牌面一致性求解。
- [puzzle-motion](.agents/skills/puzzle-motion/SKILL.md)：接入写字机式平台或 GRBL/FluidNC 并排查定位、回零和动作同步。
- [puzzle-gripper](.agents/skills/puzzle-gripper/SKILL.md)：选择并调试拼图片吸取、旋转机构与驱动电路。
- [puzzle-integration](.agents/skills/puzzle-integration/SKILL.md)：梳理拼图装置上下位机分工、参考项目和任务故障流程。
- [puzzle-evaluation](.agents/skills/puzzle-evaluation/SKILL.md)：按照 E 题规则组织整机测试、记录结果和编写设计报告。

## Monorepo 约定

已有内容：`.agents/skills`保存技能及专题知识，`docs`保存来源索引。未来按实际需要建立 `apps`（应用）、`firmware`（固件）、`hardware`（硬件）、`packages`（共享代码）。目前不预建空项目，不指定技术栈。

资料以中文 Markdown 为主，仅保留必要题图。技能按需读取配套文档；可用技能名称显式请求对应工作。

## 当前状态

基准为江苏赛区公开题面，核查日期2026-11-06。其他赛区补充规则需另查。所有工程方案均未在本项目设备上验证；Git主分支为`main`。
