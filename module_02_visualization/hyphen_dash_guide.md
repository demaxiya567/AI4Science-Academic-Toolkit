# 英文论文连字符/En-Dash/Em-Dash 三符规范

---

## 一、连字符 (Hyphen `-`)：歧义测试原则

**只有去掉连字符会产生歧义时，才加连字符。**

### 必须加连字符

| 场景 | 示例 |
|------|------|
| 名词+过去分词作形容词 | coal-fired boiler, sulfur-induced deactivation |
| X-based/supported/promoted | vanadia-based catalyst, Fe-promoted |
| 前缀 self-/post-/non-/semi- | self-cleaning, post-hoc, non-selective |
| X+Y整体修饰Z（非固定搭配） | point-estimate-based scheduling |
| 后缀 -like / -wide / -specific | site-specific, TiO₂-like |

### 不能加连字符（领域固定搭配）

| 短语 | 正确写法 | 原因 |
|------|---------|------|
| 低温转化 | low temperature conversion | 催化领域固定术语，无歧义 |
| 高温滑移 | high temperature slip | 同上 |
| 单指标监控 | single indicator monitoring | single明确修饰indicator |
| 运行条件矩阵 | operating condition matrix | 无动词成分，无歧义 |
| 钒钛催化剂 | vanadium titanium catalyst | 材料名，无歧义 |

---

## 二、En-Dash (`--` in LaTeX)：数值范围的唯一选择

**所有数值范围必须用 en-dash `--`，禁止用 hyphen `-`。**

| 场景 | 正确 | 错误 |
|------|------|------|
| 温度范围 | 150--250°C | 150-250°C |
| 浓度范围 | 28,000--58,000 h⁻¹ | 28,000-58,000 h⁻¹ |
| 比率范围 | 0.92--1.12 | 0.92-1.12 |
| 页码范围 | pp. 12--15 | pp. 12-15 |
| 年份范围 | 2020--2023 | 2020-2023 |

---

## 三、Em-Dash (`---` in LaTeX)：全面禁止

**正文中禁止任何 em-dash（`---`）。**

### 替代方案

| 优先级 | 替代 |
|--------|------|
| 1 | 逗号 , like this | 
| 2 | 括号 (like this) |
| 3 | 分号 ; |
| 4 | 拆成两句 |

---

## 四、投稿前自检命令

```bash
# 1. Em-dash 零容忍
grep -n '---' paper.tex | grep -v '^[0-9]*:[[:space:]]*%'

# 2. 不必要的领域复合词连字符
grep -n 'low-temperature\|high-temperature\|single-indicator' paper.tex

# 3. 数值范围用 hyphen 而非 en-dash
grep -n '[0-9]-[0-9]' paper.tex

# 4. 必要连字符全文一致性检查
grep -c 'coal-fired\|data-driven\|machine-readable\|site-specific' paper.tex
```
