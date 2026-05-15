# 安全批量替换流程

> 批量替换LaTeX文件时，禁止用sed直接操作tex文件（会破坏公式）。强制使用Python脚本。

---

## 替换流程

### Step 1: Python脚本替换

```python
#!/usr/bin/env python3
"""Safe batch replacement in LaTeX files."""
from pathlib import Path

def safe_replace(file_path, old, new, preview=False):
    """Replace text in a .tex file, skipping math mode environments."""
    content = Path(file_path).read_text(encoding='utf-8')
    
    # Simple approach: count occurrences
    count = content.count(old)
    if count == 0:
        return 0
    
    if preview:
        # Show surrounding context for each occurrence
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            if old in line:
                print(f"{file_path}:{i}: {line.strip()[:80]}")
        return count
    
    # Replace
    new_content = content.replace(old, new)
    Path(file_path).write_text(new_content, encoding='utf-8')
    return count


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 4:
        print("Usage: python safe_replace.py <file.tex> <old> <new> [--preview]")
        sys.exit(1)
    
    preview = '--preview' in sys.argv
    args = [a for a in sys.argv[1:] if a != '--preview']
    
    count = safe_replace(args[0], args[1], args[2], preview=preview)
    if preview:
        print(f"Found {count} occurrences")
    else:
        print(f"Replaced {count} occurrences in {args[0]}")
```

### Step 2: 预览确认

```bash
python safe_replace.py chapter3.tex "旧文本" "新文本" --preview
```

### Step 3: 执行替换

```bash
python safe_replace.py chapter3.tex "旧文本" "新文本"
```

### Step 4: 编译验证

替换后编译PDF，确认公式和交叉引用未被破坏。

---

## 禁用的命令

- ❌ `sed -i 's/old/new/g' *.tex`（sed会破坏LaTeX公式中的特殊字符）
- ❌ 直接用shell循环替换（不可控）

---

## 同类修复全局确认

替换后在**同一文件内**用grep确认所有同类问题已修复：

```bash
grep -n "旧文本" *.tex    # 应为0匹配（或预期保留数）
```
