# 文献管理工作流

> 从文献检索到BibTeX生成到投稿前审计的完整流程。

---

## 阶段1: 文献检索

```bash
# DOI → BibTeX
python scripts/doi_to_bibtex.py --dois "10.1016/j.cattod.2023.01.001"

# 批量转换（文件每行一个DOI）
python scripts/doi_to_bibtex.py --file dois.txt --output refs.bib
```

## 阶段2: 引用验证

```bash
# 检查bib中所有DOI是否可解析
python scripts/validate_citations.py --bib refs.bib
```

## 阶段3: BibTeX清理

### 常见问题
- **key命名**：统一为 `AuthorYYYY` 格式（如 `Smith2023`）
- **作者名**：`Smith, John` 格式，不同作者用 `and` 连接
- **期刊缩写**：与标准一致（如 `J. Catal.` 不是 `Journal of Catalysis`）
- **DOI**：去除多余空格/括号，格式为 `10.xxxx/xxxxx`

## 阶段4: 投稿前审计

按 `reference_audit_checklist.md` 逐项检查。
