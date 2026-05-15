# LuaLaTeX 编译规范

> 默认使用 lualatex。若期刊模板指定编译方式，以模板为准。

---

## 编译命令

```bash
# 单次编译
lualatex -interaction=nonstopmode -file-line-error <file>.tex

# 完整编译（含参考文献）
latexmk -lualatex -interaction=nonstopmode -file-line-error <file>.tex
```

### 编译前确认

执行编译前先 `ls` 确认当前目录是tex根目录（`main.tex`或目标tex所在目录）。

| 错误 ✅ | 错误 ❌ |
|---------|--------|
| `cd 正文部分/ && lualatex tjumain.tex` | 在项目根目录直接编译 |

---

## 图表浮动体铁律

1. **所有数据图一律使用 `[H]`（HERE，绝对固定）**
   - 前提：`\usepackage{float}` 已在导言区加载
   - 禁止 `[htbp]`（图会漂移到错误章节）

2. **每个section/subsection边界加 `\clearpage`**，确保浮动体不跨节

3. **图必须紧接首次引用它的段落**
   - 正确：讨论figX → figX → 讨论figY → figY
   - 错误：讨论figX → figY → figZ → 三张图堆叠

### CAS/Elsevier模板例外

如果使用 CAS 模板（`cas-sc.cls`），`[H]` 与 `float.sty` 不兼容。改用：

```latex
\noindent\begin{minipage}{\textwidth}
\centering
\includegraphics[width=\textwidth]{figures/xxx.pdf}
\captionof{figure}{Caption text.}
\label{fig:xxx}
\end{minipage}
```

---

## 禁止的命令（无模板冲突时）

- ❌ `xelatex`（除非模板要求）
- ❌ `latexmk -pdf`（默认pdflatex）
- ❌ `latexmk -xelatex`
