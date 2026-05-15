# Module 6: LaTeX 工具链

> **编译诊断、Unicode清洗、安全批量替换、表格生成**

## 核心理念

LaTeX编译的错误信息和warning来源往往难以定位——真正的错误行号与.log中的行号不一致。本模块提供从日志解析到安全替换的实用工具，解决投稿前最频繁的LaTeX摩擦。

## 包含内容

| 文件 | 用途 |
|------|------|
| `latex_diagnose.md` | LaTeX log解析与错误定位方法 |
| `latex_unicode_normalizer.md` | 投稿前Unicode字符清洗（pdflatex兼容） |
| `lualatex_compilation_guide.md` | LuaLaTeX编译规范与图表浮动体规则 |
| `safe_batch_replace.md` | 安全批量替换流程（防LaTeX公式破坏） |
| `latex_tables_template.md` | tabularray表格生成模板 |
| `compile_verify.md` | 编译后验证清单 |

## 使用流程

```bash
# 编译遇到错误时
1. 按 latex_diagnose.md 解析.log文件定位真实源文件
2. 修复错误
3. 按 lualatex_compilation_guide.md 重新编译

# 投稿前
1. 运行 latex_unicode_normalizer.md 的检查命令
2. 运行 safe_batch_replace.md 执行统一替换
3. 编译PDF并验证
```
