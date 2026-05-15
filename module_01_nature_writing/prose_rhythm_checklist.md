# 句子节奏与段落呼吸检查清单

> Nature/Science级论文的句子节奏有可量化的统计特征。用这个清单检查你的正文。

---

## 一、句长分布标准

| 区间 | 目标占比 | 功能 |
|------|---------|------|
| 短句 (5-12词) | 15-20% | 结论句、转折句、强调句 |
| 中句 (13-22词) | 45-55% | 陈述事实、描述方法、报告结果 |
| 长句 (23-35词) | 20-25% | 因果关系、条件限定、多层逻辑 |
| 超长句 (36+词) | ≤5% | 全文不超过3处 |

### 检查方法

```bash
# 用附带脚本检查
python scripts/sentence_variance_checker.py your_paper.tex
```

### 硬约束

- 句长方差 ≥ 8.0（Nature论文典型值，AI文本通常在4-6之间）
- 连续短句(≤8词) ≥3句 → 插入1句中/长句打断
- 连续长句(≥25词) ≥3句 → 插入1句短句打断

---

## 二、段落呼吸（信息密度交替）

### 定义

段落信息密度 = 新信息点数量 / 段落总词数

### 规则

- 高密度段（新信息≥3个/100词）连续 ≤ 2段
- Results每小节开头第一段 = 低密度（铺垫语境）
- Results每小节末段 = 中密度（总结但不引入新信息）
- Discussion交替：高→低→高（最后一段高密度收束）

### 自检

读三遍你写的连续三段——如果读得喘不过气，全是新数据/新发现，插入一段过渡/解释段落。

---

## 三、转场自然度

### 禁止的转场

| 禁止 | 替代 |
|------|------|
| 每段以"Furthermore/Moreover/Additionally"开头 | 用实质内容开头 |
| "Having discussed X, we now turn to Y" | 直接说Y的实质内容 |
| "Another important aspect is..." | 具体说是哪个aspect |
| 数字序号强行串联(First...Second...Third...) | 用逻辑流替代 |

### 推荐的转场模式

| 模式 | 示例 |
|------|------|
| **因果链** | "This observation raises a natural question: [具体问题]" |
| **对比锚** | "Unlike [X], where [现象], [Y] exhibits [不同]" |
| **限定递进** | "This trend holds under [条件A], but its behavior under [条件B] remains unclear" |
| **尺度跳跃** | "At the atomic scale... Scaling up to reactor conditions..." |

---

## 四、主动/被动语态比例

| 段落类型 | 主动语态 | 被动语态 |
|---------|---------|---------|
| Introduction | 60-70% | 30-40% |
| Methods | 20-30% | 70-80%（被动是惯例） |
| Results | 50-60% | 40-50% |
| Discussion | 65-75% | 25-35% |

连续3句被动语态（Methods除外）→ 将至少1句改为主动。

---

## 五、潜力叙事模板

### 语法规则（避免空洞废话）

潜力叙事必须满足以下至少2项：
1. 具体说出**能做什么**（不是"有前景"）
2. 给出**为什么能做**的逻辑连接
3. 给出**适用边界条件**
4. 给出**下一步具体步骤**

### 对照表

| 空洞写法 ❌ | 合法写法 ✅ |
|------------|------------|
| "This approach opens new avenues for catalyst design." | "The CRA analysis identifies three descriptor categories where experimental input remains essential (pore diffusion, hydrothermal aging, sulfur poisoning). Targeted measurement of these specific properties could directly improve model accuracy." |
| "Our results have important implications for SCR optimization." | "The volcano relationship in Figure 5b predicts an optimal Ce/V ratio of ~0.3 for low-temperature activity — a specific, testable hypothesis that can be validated through a focused synthesis campaign of 5-6 compositions." |
| "These findings contribute to the growing body of literature on AI-driven catalysis." | "The feature sensitivity asymmetry analysis reveals a generalizable pattern: descriptors with strong literature consensus show low sensitivity to sample size, while descriptors tied to proprietary data show high sensitivity. This pattern could serve as a diagnostic for prioritizing experimental resources." |

### 一招验证

写完一段潜力叙事，把"这个方向/这个应用/这个意义"换成具体的一件事——如果替换后读不通，原来的写法太空洞，重写。
