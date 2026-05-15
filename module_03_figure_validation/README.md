# Module 3: 图表验证与交叉引用

> **程序化验证图-文-数值一致性，不依赖人眼检查。**

## 核心理念

论文投稿前最常见的致命错误之一：正文说R²=0.92，图上标的是0.89；正文引用"Figure 3a"，图中实际只有panel (a)(b)没有(c)。这些错误靠人眼扫描很难全部抓到，程序化验证是最可靠的方式。

## 包含内容

| 文件 | 用途 |
|------|------|
| `scripts/figure_text_validator.py` | 图-文-caption数值一致性验证 |
| `scripts/cross_ref_checker.py` | 全文\ref/\cite/\includegraphics一致性 |
| `scripts/data_consistency_checker.py` | 数据统计指纹+物理合理性验证 |
| `cross_component_checklist.md` | 跨部件数值对齐检查清单 |

## 验证三角

```
Python源码（精确数值）
       ↕ 比对
LaTeX \caption{} 文本
       ↕ 比对
正文 in-text 引用和描述
```

## 使用流程

```
# Step 1: 交叉引用检查（ref/cite断裂）
python scripts/cross_ref_checker.py --tex main.tex --bib refs.bib

# Step 2: 图-文数值一致性
python scripts/figure_text_validator.py --scripts figures/*.py --tex main.tex

# Step 3: 数据统计指纹检查
python scripts/data_consistency_checker.py --csv data/*.csv --tex main.tex
```
