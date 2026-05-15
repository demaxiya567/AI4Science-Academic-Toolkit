# Claim强度分级检查清单

> 确保每个核心claim的措辞强度与证据层级匹配。不越级、不空洞。

---

## 一、Claim层级定义

| 层级 | 名称 | 定义 | 是否可当前台 |
|------|------|------|-------------|
| **L0** | 脆弱标量 | 单个 best-case 数值、单次最优值 | ❌ 不能 |
| **L1** | 局部证据 | 在单组设定内成立的局部比较 | ⚠️ 只能局部使用 |
| **L2** | 稳定结构性结论 | 跨合理扰动仍稳定的排序/分区/边界/方向 | ✅ 可作核心claim |
| **L3** | 正交收敛结论 | 多个独立证据共同支持的稳定结论 | ✅✅ 最强表述 |

---

## 二、各Section允许的Claim层级

| Section | 允许的主claim层级 | 禁止 |
|---------|-----------------|------|
| Title | L2 / L3 | L0数值做标题核心 |
| Abstract首句 | L2 / L3 问题导向 | 以best metric开场 |
| Abstract结论句 | L2 / L3 | benchmark win写成核心发现 |
| Results小节标题 | L2优先 | "性能优于基线" |
| Results段落 | L1-L3均可，主句以L2为锚 | 单次数值越级为主句 |
| Discussion | L2 / L3 | 用L0/L1推出普适机制 |
| Conclusion | L2 / L3 | 复读单次最佳数值 |
| Caption | L0/L1/L2均可 | 从单图直接外推总论 |
| Methods | 可报告L0/L1事实 | 把局部技术结果写成贡献 |

---

## 三、Evidence-to-Verb映射

| 证据层级 | 允许动词 | 慎用 |
|---------|---------|------|
| L0 | report, obtain, reach, yield | reveal, establish, demonstrate |
| L1 | indicate, support, is consistent with, suggest | prove, confirm |
| L2 | show, reveal, identify, delineate, establish | validate, confirm |
| L3 | demonstrate, confirm, validate, converge on | 无，但仍需匹配 |

### 硬规则
- `confirm / validate / demonstrate` 只能用于 **L3** 或有独立验证源
- `reveal / establish` 至少要求 **L2**
- L0/L1 不得使用因果性或机制锁定动词

---

## 四、自检流程

写完任一核心段落（Results/Discussion/Conclusion）后，对每个**主句**执行：

```
Q1: 这句话表达的是"数值"还是"结构"？
  - 数值（R²=0.95, T50=180°C, 提升19.7%）→ L0，降为supporting evidence
  - 结构（排序/边界/分区/方向/能力域）→ 继续

Q2: 这个结论在合理扰动下还成立吗？
  - 换参数/种子/数据划分还是同方向 → L2，可当前台
  - 只在单条pipeline下成立 → L1，只能局部使用

Q3: 当前section允许这种强度吗？
  - Title/Abstract结论句/Results标题/Conclusion首句 → 只允许L2/L3
  - Results段落主句 → L2优先，L1仅限技术段
  - Caption → L0/L1/L2均可，不能从单图外推总论
```

---

## 五、禁止升格为核心claim的对象

以下内容即使真实，也**不能单独**当前台：

- ❌ 单次最优数值（"最高R²=0.876"）
- ❌ 单个seed/单次split的胜负
- ❌ 纯benchmark superiority（"优于基线方法"）
- ❌ 纯速度提升（"训练时间从小时到分钟"）
- ❌ 泛化能力声称无跨体系验证

---

## 六、高风险claim防护速查

| 类型 | 默认处理 |
|------|---------|
| "first"/"首次" | 默认高风险，非必要不写 |
| "universally"/"普遍适用" | 必须有跨体系验证 |
| "prove"/"证明了"（化学机制） | 改为"support/is consistent with" |
| "outperforms all existing methods" | 改为"compares favorably with" + 具体baseline |

---

## 七、Evidence to Verb Ladder

```
L0: report / obtain / reach / yield
L1: indicate / support / is consistent with / suggest
L2: show / reveal / identify / delineate / establish
L3: demonstrate / confirm / validate / converge on
```
