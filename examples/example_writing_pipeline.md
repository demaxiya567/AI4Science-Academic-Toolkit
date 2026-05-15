# 示例：从Results写作到投稿前检查的完整pipeline

> 假设你刚完成的论文草稿，准备投 Nature Catalysis。

---

## Step 1: 写作

使用 Module 1 的 writing_engine_prompt.md 改写Results段落：

**原始版（算法为主语）**：
```
The MCFF framework achieves R²=0.876 on the NH₃-SCR dataset, outperforming all baselines by at least 12%.
```

**改写后（化学洞见为主语）**：
```
The CRA reveals a structured partition of catalytic descriptors: literature coverage is sufficient for metal loading and acidity, but pore diffusion and hydrothermal aging remain experiment-dependent blind regions.
```

## Step 2: 句子节奏检查

```bash
python module_01_nature_writing/scripts/sentence_variance_checker.py main.tex
```

检查句长方差 ≥ 8.0。如果低于8.0，混合长短句重新排版。

## Step 3: AI痕迹猎杀

运行 ai_trace_detection_checklist.md 中的 grep 命令：

```bash
grep -n -i -E "delve|landscape|leverage|cutting-edge" *.tex
```

删除或替换命中项。

## Step 4: 索赔强度检查

运行 claim_grammar_checklist.md 自检：
- 每个core claim是L2及以上？
- 动词与证据层级匹配？
- Title的主语是化学发现？

## Step 5: 绘图

使用 Module 2 的风格配置：

```python
from module_02_visualization.scripts.style_presets import configure_for_journal
configure_for_journal('nature', figure_width='single')

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
# ... 绘图代码 ...

from module_02_visualization.scripts.figure_export import save_publication_figure
save_publication_figure(fig, 'fig1_mechanism', formats=['pdf', 'png'])
```

## Step 6: 验证

```bash
# 交叉引用
python module_03_figure_validation/scripts/cross_ref_checker.py --tex main.tex --bib refs.bib

# 图-文一致
python module_03_figure_validation/scripts/figure_text_validator.py --scripts figures/*.py --tex main.tex

# 数值一致
python module_03_figure_validation/scripts/data_consistency_checker.py --tex main.tex --si SI.tex
```

## Step 7: 投稿前5分钟

```bash
# 快速检查
参照 module_04_submission/pre_submit_5min_checklist.md
```

## 完成时间线（估算）

| 步骤 | 时间 |
|------|------|
| Step 1: 写作改写 | 2-4小时 |
| Step 2-4: 质量检查 | 30分钟 |
| Step 5: 绘图 | 2-8小时 |
| Step 6: 验证 | 15分钟 |
| Step 7: 投稿前 | 5分钟 |
