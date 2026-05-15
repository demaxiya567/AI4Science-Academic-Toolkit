# AI痕迹猎杀清单

> 猎杀AI写作指纹的七个维度。每次修改正文后扫描一遍。

---

## 一、禁止过度防御叙事

### 检查项
- [ ] 有没有"需注意.../值得说明的是.../It should be noted..."类防御句？
- [ ] 有没有为已删除内容补解释？
- [ ] Caption中有没有"本图包含..."类限定语？
- [ ] 有没有"不是X而是Y"的否定式对比？
- [ ] 有没有"rather than"防御否定？
- [ ] 有没有"preliminary/suggestive/illustrative"自贬词？

### 修复策略
```
静默修复 > 删除 > 最小侵入
能改一个字不改一段话；能不加注释就不加
```

---

## 二、AI Slop词汇猎杀

### 禁止词表

| 禁止 | 替换为 |
|------|--------|
| leverage (动词) | use / employ |
| delve into | examine / investigate / analyze |
| utilize | use |
| cutting-edge | advanced / recent |
| underscores | demonstrates / shows |
| highlights | shows / reveals / indicates |
| pivotal | important / key |
| harness | use / apply |
| shed light on | clarify / elucidate / reveal |
| pave the way | enable / facilitate |
| paradigm shift | 删除，用具体描述替代 |
| nuanced | specific / detailed |
| bolster | support / strengthen |
| testament to | evidence of |
| cornerstone | foundation / basis |
| taken together | 直接给结论 |
| plethora | many / numerous |
| synergy | interaction / combination |
| compelling | strong / clear |
| nascent | emerging / early |
| endeavor | effort / work |

### 扫描命令
```bash
grep -n -i -E "delve|landscape|leverage|cutting-edge|innovative|seamless|empower|pave the way|shed light|paradigm shift|nuanced|plethora|synergy|cornerstone|testament" *.tex
```

---

## 三、Hedging堆叠禁令

**一句话最多一个hedging词。零个更好。**

| ❌ 禁止 | ✅ 正确 |
|---------|--------|
| may potentially | may 或 potentially |
| could possibly | could 或 possibly |
| it is suggested that ... might | 删掉一层 |
| appears to seemingly | appears to |

---

## 四、Hypophora禁令（自问自答）

| ❌ 禁止 | ✅ 替换 |
|---------|--------|
| "Why does X happen? Because Y." | "X happens because Y." |
| "What causes this? The key factor is..." | "This improvement stems from..." |
| "It is not X, but Y that..." | "Y, rather than X, ..." |

---

## 五、段落开头词多样性

### 禁止的连续模式

| 模式 | 修复 |
|------|------|
| 连续段以"Furthermore/Moreover/Additionally"开头 | 用实质内容开头 |
| 连续段以"However/Therefore/Thus"开头 | 混合使用不同转场 |
| "Notably/Importantly/Interestingly"频繁段落开头 | 删掉，让数据自己说话 |

---

## 六、"In this study/work"频率

**全文（Introduction到Conclusion）最多出现3次。**

替代方案：
- 直接写动作："We developed..." / "The framework achieves..."
- 省略主语直接进入内容

---

## 七、Conclusion ≠ Abstract

- [ ] Conclusion是否逐句复述了Abstract？（相似度>60% = ❌）
- [ ] Conclusion是否包含：(1)核心发现凝练 (2)与领域关系 (3)局限性 (4)展望？

---

## 八、语义空洞句禁令

### 检测方法
删掉该句，段落是否丢失信息？
- 不丢 = 语义空洞句，删除
- 丢 = 保留

### 高风险句式

| 禁止 | 原因 |
|------|------|
| "This approach opens new avenues for..." | 没说什么avenues |
| "These results have important implications for..." | 没说哪些implications |
| "The findings contribute to the growing body of literature..." | 学术废话 |
| "plays a crucial/pivotal/vital role in..." | AI万能搭配 |
| "shed light on the underlying mechanism" | 没说什么mechanism |

### 密度阈值
每1000词 ≤1处空洞句。

---

## 九、中文AI指纹（大论文用）

| 检查项 | 阈值 |
|--------|------|
| CRITICAL级AI专属词（值得注意的是/需要指出的是/具有广阔的应用前景） | 0次 |
| 本章/本文/本研究（学位论文自指） | ≤5次/千字 |
| 进一步/进而/具体而言/换言之 | ≤2-3次/章 |
| 首先...其次...最后 | 每章≤2次 |
| 随着...的发展 | 全文≤1次 |
