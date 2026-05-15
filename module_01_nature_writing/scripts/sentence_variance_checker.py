#!/usr/bin/env python3
"""
句长方差检测器 — 快速评估学术写作的句子节奏。

用法:
    python sentence_variance_checker.py paper.tex
    python sentence_variance_checker.py paper.tex --min-variance 8.0

Nature子刊目标:
    - 句长方差 ≥ 8.0（AI文本通常在4-6之间）
    - 平均句长 15-22词
    - 短句(≤8词)占比 15-20%
    - 长句(≥25词)占比 20-25%
"""

import re
import sys
from pathlib import Path


def extract_sentences(text: str):
    """从LaTeX文本提取句子，忽略公式、注释和bib条目"""
    # 去掉注释行
    text = re.sub(r'(?<!\\)%.*', '', text)
    # 去掉公式环境
    text = re.sub(r'\$.*?\$', '', text)
    text = re.sub(r'\$\$.*?\$\$', '', text, flags=re.DOTALL)
    text = re.sub(r'\\begin\{equation\}.*?\\end\{equation\}',
                  '', text, flags=re.DOTALL)

    # 按句号/问号/感叹号分句
    sentences = re.split(r'(?<=[.!?])\s+', text)
    # 过滤太短的片段和命令行
    sentences = [s.strip() for s in sentences
                 if s.strip() and len(s.split()) >= 3
                 and not s.strip().startswith('\\')]
    return sentences


def report(text_path):
    text = Path(text_path).read_text(encoding='utf-8', errors='ignore')
    sents = extract_sentences(text)

    if not sents:
        print("⚠️  未能提取到有效句子。检查文件格式。")
        return

    lens = [len(s.split()) for s in sents]

    import statistics
    variance = statistics.pvariance(lens)
    mean_len = statistics.mean(lens)

    short_ratio = sum(1 for l in lens if l <= 8) / len(lens)
    long_ratio = sum(1 for l in lens if l >= 25) / len(lens)
    medium_ratio = sum(1 for l in lens if 13 <= l <= 22) / len(lens)

    print("=" * 55)
    print("  句子节奏分析报告")
    print("=" * 55)
    print(f"  总句数:      {len(lens)}")
    print(f"  平均句长:     {mean_len:.1f} 词")
    print(f"  句长方差:     {variance:.1f}  {'✅' if variance >= 8 else '⚠️  < 8.0'}")
    print(f"  句长标准差:   {statistics.stdev(lens):.1f}")
    print(f"  最短:        {min(lens)} 词 | 最长: {max(lens)} 词")
    print()
    print(f"  短句(≤8词):  {short_ratio*100:.1f}%  ", end="")
    if short_ratio < 0.10:
        print("⚠️  低于建议的15-20%")
    elif short_ratio > 0.30:
        print("⚠️  高于建议的15-20%")
    else:
        print("✅")

    print(f"  中句(13-22词): {medium_ratio*100:.1f}%  ", end="")
    if 0.40 <= medium_ratio <= 0.60:
        print("✅")
    else:
        print("⚠️  建议45-55%")

    print(f"  长句(≥25词):  {long_ratio*100:.1f}%  ", end="")
    if long_ratio > 0.30:
        print("⚠️  高于建议的20-25%")
    elif long_ratio < 0.15:
        print("⚠️  低于建议的20-25%")
    else:
        print("✅")

    print()

    # 检查连续短句/长句
    short_runs = 0
    long_runs = 0
    for l in lens:
        if l <= 8:
            short_runs += 1
        else:
            short_runs = 0
        if short_runs >= 3:
            print(f"⚠️  连续{short_runs}句短句(≤8词) — 需要插入中/长句打断")

    for l in lens:
        if l >= 25:
            long_runs += 1
        else:
            long_runs = 0
        if long_runs >= 3:
            print(f"⚠️  连续{long_runs}句长句(≥25词) — 需要插入短句打断")

    print()
    if variance >= 8 and 0.10 <= short_ratio <= 0.30 and 0.15 <= long_ratio <= 0.30:
        print("✅ 句子节奏符合Nature子刊标准")
    else:
        print("💡 建议: 混合短句(5-12词)和长句(23-35词)，增加句长方差")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("用法: python sentence_variance_checker.py <paper.tex>")
        sys.exit(1)
    report(sys.argv[1])
