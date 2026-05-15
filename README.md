# AI4Science Academic Toolkit

> **Nature级学术出版工具包 · 面向生化环材+AI for Science研究者**
> 不会写论文？不会调图表？投稿前总漏掉致命错误？这个工具包就是帮你解决这些问题的。

**作者**: 童成峥（天津大学环境科学与工程学院，博士研究生）
**GitHub**: 欢迎 Star / Fork / PR — 让更多被论文折磨的博士生看到

---

## 📖 这个工具包是干什么的？

如果你在生化环材领域做 AI for Science 研究（机器学习+催化/材料/环境），你会发现写论文有几件特别烦的事：

1. **不会写"Nature味"的论文** — 明明数据很好，写出来编辑就是不爱看
2. **图表总是被审稿人挑毛病** — 颜色不对、字体不统一、DPI不够
3. **投稿前心里没底** — 引用是不是假的？正文和SI数值一致吗？图序对不对？
4. **LaTeX编译报错看不懂** — 每次编译都出一堆 warning，不知道哪些该修

本工具包把这四件事打包成了 **6个模块**，每个模块都有：
- ✅ 给 AI 用的写作 prompt（直接复制给 Claude/GPT）
- ✅ Python 脚本（一键运行）
- ✅ 检查清单（打印出来打勾）
- ✅ 模板（填空就能用）

---

## 🚀 快速安装（2分钟）

### 方法一：直接下载（最简单）

```bash
# 1. 克隆仓库
git clone https://github.com/demaxiya567/AI4Science-Academic-Toolkit.git
cd AI4Science-Academic-Toolkit

# 2. 安装 Python 依赖
pip install -r requirements.txt
```

**如果不会用 git**：去 GitHub 页面点绿色的 `Code` → `Download ZIP`，解压就行。

### 方法二：在 Claude Code 中使用

```bash
# 1. 克隆
git clone https://github.com/demaxiya567/AI4Science-Academic-Toolkit.git
cd AI4Science-Academic-Toolkit

# 2. 启动 Claude Code
claude

# 3. 然后你就可以对 Claude 说：
#    "用 module_01 的 writing_engine_prompt.md 帮我改Abstract"
#    "用 module_02 的 checklists 检查我的图"
#    "运行 module_03 的 cross_ref_checker.py 检查引用"
```

### 方法三：在 Codex / Cursor / Windsurf 中使用

```bash
# 1. 克隆仓库
git clone https://github.com/demaxiya567/AI4Science-Academic-Toolkit.git

# 2. 在 AI 工具中打开项目目录
# 3. 把对应模块的 prompt 文件内容复制给 AI
# 4. 或者直接对 AI 说：读一下 module_01/README.md 然后按里面的步骤做
```

---

## 📦 六大模块详解

### 模块1：Nature级写作引擎 📝

**你遇到的问题**：写出来的 Introduction 像文献综述，Results 像实验记录，缺乏"故事感"。

**这个模块怎么帮你**：提供了一套"Nature子刊编辑看了就想送审"的写作模板和检查工具。

```
📁 module_01_nature_writing/
├── narrative_arc_checklist.md     ← 论文结构检查——三幕节奏、证据阶梯、流汇聚
├── writing_engine_prompt.md      ← 【推荐】直接复制给AI的写作prompt
├── prose_rhythm_checklist.md     ← 检查句子节奏（AI写作一眼就能看出来的问题）
├── ai_trace_detection_checklist.md  ← 猎杀AI写作痕迹（审稿人最烦的词汇列表）
├── claim_grammar_checklist.md    ← 检查结论吹没吹过头
├── templates/
│   └── nature_sub_templates.md   ← Abstract/Introduction/Results模板
└── scripts/
    └── sentence_variance_checker.py  ← 自动检测句长方差
```

**使用步骤**：
```
第1步：把你写好的草稿给AI，同时复制 writing_engine_prompt.md 的内容
      → AI 会按 Nature 子刊标准重写

第2步：运行句子节奏检查
      python module_01_nature_writing/scripts/sentence_variance_checker.py 你的论文.tex

第3步：用 ai_trace_detection_checklist.md 扫描AI痕迹
      → 把 those leverage/delve/cutting-edge 全部干掉

第4步：用 claim_grammar_checklist.md 确认核心结论没吹过头
```

---

### 模块2：可视化规范与工具 🎨

**你遇到的问题**：图做好了，但总觉得配色奇怪、字体和正文不统一、投稿时才知道DPI不够。

**这个模块怎么帮你**：提供了色盲友好配色 + 期刊尺寸预设 + 一键导出的全套工具。

```
📁 module_02_visualization/
├── figure_style_standard.md      ← 先读这个：字号/字体/DPI/参考线规范
├── visual_persuasion_checklist.md  ← 图做完了用这个检查
├── hyphen_dash_guide.md          ← 英文论文连词符规范
├── decimal_precision_guide.md    ← 数值精度（避免"一眼假"）
├── title_case_guide.md           ← 标题大小写（不同期刊不同规则）
├── drawio_convention.md          ← 流程图命名规范
├── scripts/
│   ├── figure_export.py          ← 一键导出PDF+PNG+SVG（三格式）
│   ├── style_presets.py          ← 设置期刊风格（Nature/ACS/RSC）
│   └── figure_validator.py       ← 自动检查DPI/字体/CJK兼容性
└── assets/
    ├── color_palettes.py         ← 色盲友好配色（Okabe-Ito / Paul Tol）
    ├── nature.mplstyle            ← Nature风格配置文件
    ├── publication.mplstyle       ← 通用出版风格
    └── journal_requirements.md    ← 各期刊图表尺寸要求速查
```

**使用步骤**（以 Python matplotlib 为例）：
```python
# 在你的绘图脚本开头加上：
from module_02_visualization.scripts.style_presets import configure_for_journal
from module_02_visualization.scripts.figure_export import save_publication_figure

# 设置期刊风格（一行代码搞定所有字体/字号/尺寸）
configure_for_journal('nature', figure_width='single')

# 正常画图
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('Temperature (°C)')
ax.set_ylabel('Conversion (%)')

# 一键导出（PDF给LaTeX用，PNG给预览，SVG给检查）
save_publication_figure(fig, 'my_figure', formats=['pdf', 'png'])
```

**如果不会用 Python**：复制 `figure_style_standard.md` 里的规范给你的合作者或润色公司看。

---

### 模块3：图表验证与交叉引用 ✅

**你遇到的问题**：投稿前最怕"正文写R²=0.92，图上标的是0.89"这种低级错误。

**这个模块怎么帮你**：程序化检查，不用人眼一行行对。

```
📁 module_03_figure_validation/
├── scripts/
│   ├── cross_ref_checker.py      ← 检查所有 \ref 和 \cite 有没有断裂
│   ├── figure_text_validator.py   ← 对比Python脚本数值 vs LaTeX caption
│   └── data_consistency_checker.py ← 检查正文和SI数值是否一致
├── cross_component_checklist.md   ← 跨部件对齐检查
└── README.md
```

**使用步骤**：
```bash
# 1. 交叉引用检查（有没有ref断裂）
python module_03_figure_validation/scripts/cross_ref_checker.py --tex main.tex --bib refs.bib

# 2. 图-文数值一致性
python module_03_figure_validation/scripts/figure_text_validator.py --scripts figures/*.py --tex main.tex

# 3. 数据一致性（正文 vs SI）
python module_03_figure_validation/scripts/data_consistency_checker.py --tex main.tex --si SI.tex
```

---

### 模块4：投稿前全流程 Pipeline 🏭

**你遇到的问题**：要投稿了，心里没底——有没有什么致命错误漏掉了？

**这个模块怎么帮你**：11步检查流程 + 5分钟快速扫描 + 编辑速览模拟。

```
📁 module_04_submission/
├── submission_pipeline.md           ← 完整11步投稿流程
├── pre_submit_5min_checklist.md     ← 【推荐】5分钟快速扫一遍
├── editor_gatekeeper_checklist.md   ← 模拟编辑5分钟决策
└── submission_readiness_checklist.md ← 判断"能不能投了"
```

**紧急情况**（明天就要投了）：
```
只看 pre_submit_5min_checklist.md 里的5项：
1. 虚假引用（最高风险！）
2. 正文-SI数值矛盾
3. 图表问题（图序/位置/DPI）
4. 作者/单位/基金信息
5. 格式致命问题
```

---

### 模块5：文献管理与引用审查 📚

**你遇到的问题**：AI 写的论文经常出现"幻觉引用"——引用了一篇根本不存在的论文。

**这个模块怎么帮你**：DOI→BibTeX批量转换 + 引用真实性验证。

```
📁 module_05_citation/
├── scripts/
│   ├── doi_to_bibtex.py           ← DOI批量转BibTeX
│   └── validate_citations.py      ← 检查DOI是否真实存在
├── reference_audit_checklist.md    ← 投稿前参考文献检查
├── reference_reality_check.md      ← LLM幻觉引用专项检查
└── citation_workflow.md            ← 完整工作流
```

**使用步骤**：
```bash
# DOI → BibTeX
python module_05_citation/scripts/doi_to_bibtex.py --dois "10.1016/j.cattod.2023.01.001"

# 检查引用真实性
python module_05_citation/scripts/validate_citations.py --bib refs.bib
```

---

### 模块6：LaTeX工具链 🔧

**你遇到的问题**：编译报错看不懂、Unicode字符导致编译失败、批量替换破坏了公式。

**这个模块怎么帮你**：日志定位 + Unicode清洗 + 安全批量替换。

```
📁 module_06_latex_toolchain/
├── latex_diagnose.md               ← 日志解析和错误定位
├── lualatex_compilation_guide.md   ← LuaLaTeX编译规范
├── latex_unicode_normalizer.md     ← Unicode字符清洗
├── safe_batch_replace.md           ← 安全批量替换
├── latex_tables_template.md        ← 表格生成模板
└── compile_verify.md               ← 编译后检查清单
```

---

## 🔧 我是零基础，从哪开始？

| 你现在的处境 | 先看这个 |
|------------|---------|
| 论文刚写完初稿，想改得更好 | `module_01_nature_writing/writing_engine_prompt.md` |
| 图已经画好了，但觉得不好看 | `module_02_visualization/figure_style_standard.md` |
| 明天就要投稿了 | `module_04_submission/pre_submit_5min_checklist.md` |
| LaTeX编译报错看不懂 | `module_06_latex_toolchain/latex_diagnose.md` |
| 想检查引用有没有问题 | `module_05_citation/validate_citations.py` |
| 所有步骤都想走一遍 | 按顺序看 module_01 → 02 → 03 → 04 |

---

## 🤖 怎么用 AI 配合这个工具包

### 在 Claude Code 中使用

```bash
# 启动 Claude Code
claude

# 然后直接说：
# "读一下 module_01_nature_writing/writing_engine_prompt.md 的内容，
#  然后用它对这篇文章做个Nature风格的改写"
```

### 在 ChatGPT / Claude 网页版中使用

**最简单的方式**：打开对应模块的 `.md` 文件，全选复制，粘贴给 AI，再加上你的论文内容。

### 在 Codex 中使用

```bash
codex -C "你的论文目录" "按 module_04_submission/pre_submit_5min_checklist.md 检查我的论文"
```

---

## 📋 系统要求

- **Python**: 3.8+
- **依赖**: `pip install -r requirements.txt`（主要是 matplotlib, numpy, pandas）
- **LaTeX**: 推荐 LuaLaTeX（module_6 工具链）
- **AI 工具**: Claude / ChatGPT / Codex 任选（module_1 需要）

---

## 🤝 如何贡献

1. Fork 本仓库
2. 创建你的分支: `git checkout -b my-feature`
3. 提交: `git commit -am 'Add something'`
4. Push: `git push origin my-feature`
5. 开一个 Pull Request

任何能帮助生化环材博士生更好发论文的贡献都欢迎！

---

## 📄 License

MIT License — 随便用，随便改，随便发。

---

**Star ⭐ 这个仓库，让更多被论文折磨的博士生看到。**
