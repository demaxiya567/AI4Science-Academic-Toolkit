# 图表视觉规范（跨论文通用）

> 同一本论文/同一次投稿中所有图必须视觉统一。

---

## 一、字体规范

### 大论文（博士毕业论文）

| 元素 | 字体 | 说明 |
|------|------|------|
| 中文 | 宋体 (SimSun) | — |
| 英文+数字 | Times New Roman | — |
| math mode | Times New Roman | — |

### 小论文（SCI期刊投稿）

| 期刊类型 | 推荐字体 | 说明 |
|---------|---------|------|
| Nature系列 | Arial / Helvetica | — |
| ACS/RSC系列 | Arial | — |
| Elsevier系列 | Arial 或 Times New Roman | 全文统一 |

### CJK + mathtext 铁律

中文字符**绝对禁止**出现在 `$...$` math mode 内（matplotlib parser会崩溃）。
混排方案：中文用独立 `plt.text()`，数学符号用unicode替代（σ/²/±/×/→）。

---

## 二、字号层级

| 元素 | 字号 | rcParams key |
|------|------|-------------|
| 基础字号 | 12pt | font.size |
| 轴标签 | 13pt | axes.labelsize |
| 子图标题 | 14pt | axes.titlesize |
| 图例 | 11pt | legend.fontsize |
| 刻度标签 | 11pt | xtick/ytick.labelsize |
| Panel标签 | 16pt bold | 手动 text() |
| 图内标注 | 10pt | — |

---

## 三、颜色规范

### 统一方法颜色表

同一方法/模型在整本论文中颜色必须一致。在 `color_palettes.py` 中定义：

```python
METHOD_COLORS = {
    'Your_Method': '#B2182B',   # 深红
    'Reference':   '#2166AC',   # 深蓝
    'Baseline_1':  '#4D4D4D',   # 中灰
    'Baseline_2':  '#878787',   # 浅灰
}
```

### 色盲友好

默认使用 Paul Tol 或 Okabe-Ito 色盲友好调色板。避免红+绿同时作为区分依据。

### 推荐配色方案

```python
# Okabe-Ito（所有色盲类型可区分）
OKABE_ITO = ['#E69F00', '#56B4E9', '#009E73', '#F0E442',
             '#0072B2', '#D55E00', '#CC79A7', '#000000']

# Paul Tol Bright
TOL_BRIGHT = ['#4477AA', '#EE6677', '#228833', '#CCBB44',
              '#66CCEE', '#AA3377', '#BBBBBB']
```

---

## 四、参考线规范

| 语义 | linestyle | 颜色 | 示例 |
|------|----------|------|------|
| 零线/基准线 | `'--'` dashed | `'#999999'` 灰 | y=0, x=0 |
| 目标阈值 | `':'` dotted | `'#999999'` 或主色 | R²=0.85目标线 |
| 危险区/边界 | `'--'` dashed | `'#B71C1C'` 深红 | — |
| 收敛标记 | `'-.'` dashdot | `'#2E7D32'` 深绿 | — |

---

## 五、DPI与输出格式

```python
DPI_PREVIEW = 150   # 交互预览
DPI_SAVE = 600      # 保存输出（PNG）
```

每个 `savefig` 必须同时输出 SVG + PDF + PNG：
- PDF：LaTeX `\includegraphics` 插入
- SVG：文本审查
- PNG：肉眼预览

---

## 六、参考figsize

| 用途 | figsize | 适用 |
|------|---------|------|
| 单栏图 | (7, 5) | 大论文/小论文单图 |
| 双栏宽图 | (14, 5) | 并排对比、多panel |
| 方形图 | (7, 7) | 热力图、混淆矩阵 |
| 多panel组合 | (14, 10) | 2×2或2×3布局 |

---

## 七、Panel标注统一函数

```python
def add_panel_label(ax, label, x=-0.08, y=1.06,
                    fontsize=16, fontweight='bold'):
    ax.text(x, y, label, transform=ax.transAxes,
            fontsize=fontsize, fontweight=fontweight,
            va='bottom', ha='right')
```
