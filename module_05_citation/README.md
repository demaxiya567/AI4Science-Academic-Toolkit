# Module 5: 文献管理与引用审查

> **DOI→BibTeX批量转换、引用真实性验证、参考文献格式清洗**

## 核心理念

LLM幻觉引用（论文不存在、作者拼错、DOI虚构）是2023-2026年撤稿的最高频原因之一。本模块提供从文献检索到投稿前引用审计的完整工具链。

## 包含内容

| 文件 | 用途 |
|------|------|
| `citation_workflow.md` | 从文献检索到BibTeX生成的完整工作流 |
| `reference_audit_checklist.md` | 投稿前参考文献审查清单 |
| `reference_reality_check.md` | 引用真实性检查（针对LLM幻觉） |
| `scripts/doi_to_bibtex.py` | DOI→BibTeX批量转换（通过Crossref API） |
| `scripts/validate_citations.py` | 引用真实性批量验证 |
| `scripts/extract_metadata.py` | 从文献数据提取元数据 |

## 使用流程

```bash
# Step 1: DOI → BibTeX
python scripts/doi_to_bibtex.py --dois "10.1016/j.cattod.2023.01.001" "10.1021/acscatal.3c01234"

# Step 2: 引用真实性批量验证
python scripts/validate_citations.py --bib refs.bib

# Step 3: 按reference_audit_checklist手动检查格式
```
