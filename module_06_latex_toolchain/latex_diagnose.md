# LaTeX 错误/警告精确诊断

> **永远从.log文件出发，不猜测。**

---

## 核心原则

### 从log定位真实源文件

LaTeX的错误行号在嵌套 `\input` 后偏移，真正的错误可能不在主文件中。通过括号嵌套解析找到活跃文件：

```latex
(./main.tex             ← 当前活跃文件
  (./chapters/intro.tex ← 嵌套输入
    (./figures/fig1.tex)
  )
)
```

### 成品优先

| 优先级 | 处理 |
|--------|------|
| **必须修** | 没有生成PDF / 编译中断 / PDF中出现`??`/缺图/越界 |
| **默认不修** | `duplicate destination` / 字体替代 / nonstopmode下的非阻断warning |

---

## 检查命令

```bash
# 提取所有warnings和errors
# Overfull hbox
grep -n "Overfull \\\\hbox" main.log

# Missing references
grep -n "LaTeX Warning: Reference.*undefined" main.log

# Missing citations
grep -n "LaTeX Warning: Citation.*undefined" main.log

# 确认PDF生成
grep "Output written on" main.log
```

---

## 输出报告格式

```
# LaTeX 诊断报告

## Errors (必须修复)
| # | 源文件 | 行号 | 类型 | 内容 | 修复建议 |

## Warnings (建议修复)
| # | 源文件 | 行号 | 类型 | 内容 | 修复建议 |

## Missing References/Citations
| # | 类型 | 键 | 首次出现位置 |
```

---

## 常见错误速查

| 错误 | 最常见原因 | 修复 |
|------|-----------|------|
| `! Undefined control sequence` | 缺少宏包 | 在导言区加入`\usepackage{...}` |
| `! File not found` | 图片路径或文件名错误 | 确认文件名大小写和路径 |
| `! Missing $ inserted` | math mode内外混排 | 检查`$...$`是否成对 |
| `Overfull \\hbox` | 内容超出页宽 | 换行、调整表格或使用`\sloppy` |
