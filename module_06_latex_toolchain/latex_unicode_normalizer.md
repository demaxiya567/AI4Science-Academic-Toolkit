# LaTeX Unicode字符规范化

> **投稿前将tex文件中所有非ASCII Unicode字符替换为LaTeX命令，确保pdflatex编译通过。**

---

## 检查命令

```bash
# 扫描非ASCII字符
grep -n -P '[^\x00-\x7F]' main.tex SI.tex

# 常见字符替换
# 长破折号 — → ---
# 韩文破折号 → ---
# 左右引号 "" → ""
# 省略号 … → \dots{}
# 乘号 × → \times
# 度 ° → \textdegree{} 或 $^\circ$
# 希腊字母 α → $\alpha$ 等
# 上标/下标字符 ² → $^2$ 等
```

---

## 常见问题

| 字符 | 问题 | 解决方案 |
|------|------|---------|
| UTF-8引号 `""` | pdflatex无法渲染 | 替换为ASCII `""` |
| 中文全角空格 | pdflatex编译错误 | 替换为半角或 `\hspace{}` |
| Emoji | 无法渲染 | 删除或替换为文字描述 |
| 非ASCII数学符号 | pdflatex报错 | 替换为 `$...$` 内LaTeX命令 |
