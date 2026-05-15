# 投稿前全流程检查Pipeline

> 11步流程，增量执行，避免context爆炸。每一步完成后将结果写入 pipeline_report/ 目录。

---

## Step 0: 文件确认（必须）

**投稿模式确认**：

| 模式 | 需要文件 | 适用期刊 |
|------|---------|---------|
| **docx投稿** | 正文docx + SI docx + 图片目录 | NC, NMI等 |
| **LaTeX投稿** | 正文tex + SI tex + bib + 图片目录 | ACS, RSC, Elsevier等 |

确认后将文件清单写入 `pipeline_report/00_file_scope.md`。

---

## Step 1: 编辑速览模拟

模拟编辑5分钟desk review决策：

| 检查项 | 标准 |
|--------|------|
| Title | 有化学发现的味道？非"Development of Y framework" |
| Abstract首句 | 化学问题的urgency？非方法论陈述 |
| Abstract结论句 | 化学发现/预测？非R²数值 |
| Fig.1 | 独立传达核心发现？ |
| Results标题 | 每个标题含化学信息？ |

---

## Step 2: 数值一致性检查

运行模块3脚本：

```bash
# 交叉引用检查
python module_03_figure_validation/scripts/cross_ref_checker.py --tex main.tex --bib refs.bib

# 图-文数值
python module_03_figure_validation/scripts/figure_text_validator.py --scripts figures/*.py --tex main.tex

# 终端数据
python module_03_figure_validation/scripts/data_consistency_checker.py --tex main.tex --si SI.tex
```

---

## Step 3: AI写作痕迹检测

运行模块1检查清单：

- [ ] AI slop词汇密度 ≤ 2次/1000词
- [ ] 句长方差 ≥ 8.0
- [ ] 语义空洞句 ≤ 1处/1000词
- [ ] "In this study/work" ≤ 3次全文
- [ ] 无 "rather than" 防御否定
- [ ] 无 "notably/importantly/crucially" 连续段落开头

---

## Step 4: 参考文献审计

- [ ] 所有DOI可解析
- [ ] 无LLM幻觉引用（2023-2026年发表、小众期刊组合重点关注）
- [ ] 自引确认准确
- [ ] BibTeX格式与期刊要求一致

---

## Step 5: 图表技术验证

- [ ] 所有图在当前编译器下可渲染（pdflatex/LuaLaTeX）
- [ ] DPI ≥ 300（光栅图）或矢量格式
- [ ] 所有中文字符不在 $...$ math mode内
- [ ] 图序连续（无跳号）
- [ ] 图在PDF中的页码与所属section匹配

---

## Step 6: 逻辑连贯性审查

- [ ] 跨段因果链一致（无A→B和B不依赖于A同时出现）
- [ ] 方法适用范围一致（Methods→Results→Discussion无矛盾）
- [ ] Discussion不重复Results数据

---

## Step 7: Go/No-Go决策

| 级别 | 判定 | 动作 |
|------|------|------|
| 🔴 FATAL | 虚假引用、数值矛盾、严重逻辑错误 | 禁止投稿，必须修复 |
| 🟠 MAJOR | claim越级、AI痕迹超标、写作问题 | 修复后重新审查 |
| 🟢 PASS | 全部通过 | 可以投稿 |

---

## 快速模式（时间紧迫）

只执行 Step 0 + Step 2 + Step 4（最高风险检查），其余步骤跳过。完成后在 pipeline_report 中标记 "QUICK MODE"。
