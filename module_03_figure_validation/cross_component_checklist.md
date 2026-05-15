# 跨部件数据对齐检查清单

> 确保正文/图/表/SI之间同一数值完全一致。

---

## 检查项

### 正文 ↔ 表格
- [ ] 正文中引用的数值与所在表格中的数值一致
- [ ] 同一指标在正文不同位置（body/table/caption）一致

### 正文 ↔ 图
- [ ] 正文引用的R²/MAE/T50等与图中标注一致
- [ ] Caption描述的视觉元素在图中确实存在

### 正文 ↔ SI
- [ ] 正文引用的Figure S编号在SI中存在
- [ ] 正文数值与SI对应数值一致

### 表 ↔ 图
- [ ] 同一指标在表和图中的精度一致（如R²都到3位小数）

### 跨章引用
- [ ] 同一基线数值在各章中一致（大论文用）

---

## 执行命令

```bash
# 交叉引用（ref/cite断裂）
python module_03_figure_validation/scripts/cross_ref_checker.py --tex main.tex --bib refs.bib

# 图-文数值
python module_03_figure_validation/scripts/figure_text_validator.py --scripts figures/*.py --tex main.tex

# 终端数据
python module_03_figure_validation/scripts/data_consistency_checker.py --tex main.tex --si SI.tex
```
