# draw.io 图表规范

> 管理 draw.io 源文件的命名、导出、字体和目录清洁。

---

## 一、命名规范

### 格式
```
fig_ch{N}_{序号}_{英文描述}.drawio
```

### 示例
```
✅ fig_ch1_01_research_framework.drawio
✅ fig_ch3_05_cra_mechanism.drawio
❌ 图3-1.drawio（中文命名）
❌ Figure 1.drawio（含空格）
```

### 规则
- 文件名全英文、全小写、下划线分隔
- 禁止中文字符、空格
- 版本管理用git，不用"备用"/"old"/"v2"后缀

---

## 二、导出协议

每次修改 `.drawio` 源文件后，必须立即重导出：

| 格式 | 用途 | 命名 |
|------|------|------|
| **PDF** | LaTeX插入 | `fig_ch1_01_xxx.drawio.pdf` |
| **SVG** | 文本审查 | `fig_ch1_01_xxx.drawio.svg` |
| **PNG**（可选） | 快速预览 | `fig_ch1_01_xxx_preview.png` |

### 导出步骤（draw.io桌面版）
1. File → Export as → PDF（勾选 Embed fonts, Scale: 100%）
2. File → Export as → SVG（勾选 Embed fonts）

---

## 三、字体白名单

| 类别 | 推荐字体 |
|------|---------|
| 无衬线（主力） | **Arial** / Helvetica |
| 衬线 | **Times New Roman** |
| 中文 | **宋体**（SimSun） |
| 等宽 | **Consolas** / Courier New |

### 禁止使用的字体
- ❌ **微软雅黑**（PDF嵌入在部分系统渲染异常）
- ❌ **黑体**（SimHei）
- ❌ Comic Sans / Papyrus

---

## 四、draw.io vs matplotlib 职责划分

| 图表类型 | 工具 | 理由 |
|---------|------|------|
| 流程图/架构图/概念图 | **draw.io** | 连接线+布局+图标 |
| 数据图（散点/柱/折线） | **matplotlib** | 数据驱动 |
| 机理示意图 | **draw.io** | 自由排版+箭头 |
| 算法流程/伪代码图 | **draw.io** | 结构化流程 |
| 对比表（视觉化） | matplotlib 或 LaTeX tabular | 取决于复杂度 |

**禁止**：同一概念图同时存在draw.io版和matplotlib版（二选一）。
