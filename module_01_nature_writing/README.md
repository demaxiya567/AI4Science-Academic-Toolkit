# Module 1: Nature-Level Writing Engine

> **让AI for Science论文的叙事达到Nature子刊水准**

## 核心理念

**化学洞见优先，算法是引擎，洞见是产品。编辑买产品不买引擎。**

生化环材论文的审稿人和编辑首先看的是**科学发现**，不是算法benchmark。这个模块帮你把技术内容包装成编辑和审稿人愿意读的故事。

## 包含内容

| 文件 | 用途 |
|------|------|
| `writing_engine_prompt.md` | AI写作prompt模板——告诉AI按Nature子刊标准写作 |
| `prose_rhythm_checklist.md` | 句子节奏检查——句长方差、段落呼吸、转场自然度 |
| `ai_trace_detection_checklist.md` | AI痕迹猎杀清单——词汇级+结构级双重检查 |
| `claim_grammar_checklist.md` | Claim强度分级——确保核心claim不越级、不空洞 |
| `templates/` | Abstract / Introduction / Results / Discussion 写作模板 |
| `scripts/sentence_variance_checker.py` | 句长方差检测脚本 |

## 使用流程

```
Step 1: 把你的数据和初步结果写好
Step 2: 用 writing_engine_prompt.md 提示AI改写正文
Step 3: 用 prose_rhythm_checklist.md 检查句子节奏
Step 4: 用 ai_trace_detection_checklist.md 猎杀AI痕迹
Step 5: 用 claim_grammar_checklist.md 确认核心claim不越级
Step 6: 参考 templates/ 调整结构
```

## 适用场景

- 新论文从零写Abstract/Introduction/Results/Discussion
- 已有稿件改写以提高发表概率
- Discussion/Conclusion空洞，需要填充有实质的潜力叙事
- 审稿人说"写作需要大幅提升"