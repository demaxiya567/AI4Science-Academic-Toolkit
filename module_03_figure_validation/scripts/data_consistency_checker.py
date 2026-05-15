#!/usr/bin/env python3
"""
Data Consistency Validator: cross-check data consistency and statistical fingerprints.

Usage:
    python data_consistency_checker.py --csv data/*.csv --tex main.tex
    python data_consistency_checker.py --tex main.tex --si SI.tex
"""

import re
import csv
import argparse
from pathlib import Path
from collections import Counter


def extract_tex_numbers(tex_path):
    text = Path(tex_path).read_text(encoding='utf-8', errors='ignore')
    patterns = {
        "r2": r"R\^?\{?2\}?\s*[=≈]\s*(0\.\d{2,4})",
        "rmse": r"RMSE\s*[=≈]\s*(\d+\.?\d*)",
        "mae": r"MAE\s*[=≈]\s*(\d+\.?\d*)",
        "t50": r"T_?\{?50\}?\s*[=≈]\s*(\d+)",
        "t90": r"T_?\{?90\}?\s*[=≈]\s*(\d+)",
        "pct": r"(\d{1,3}\.?\d*)\s*\\?%",
    }
    found = {}
    for key, pat in patterns.items():
        matches = re.findall(pat, text)
        if matches:
            found[key] = [float(m) for m in matches]
    return found


def check_tail_distribution(numbers):
    if not numbers:
        return
    decimals = [round(v % 1, 2) for v in numbers if v % 1 != 0]
    if not decimals:
        return
    last_digits = [str(d)[-1] for d in decimals]
    counter = Counter(last_digits)
    total = len(last_digits)
    issues = []
    for d in '0123456789':
        pct = counter.get(d, 0) / total * 100
        if pct > 20:
            issues.append(f"  ⚠️ 尾数.{d}: {pct:.1f}% (>20%)")
        elif pct < 4 and total >= 20:
            issues.append(f"  ⚡ 尾数.{d}: {pct:.1f}% (<4%)")
    return issues


def check_csv_fingerprint(csv_path):
    rows = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            for cell in row:
                try:
                    rows.append(float(cell))
                except ValueError:
                    pass
    if not rows:
        return []

    issues = []

    # Round number ratio
    round_ints = [v for v in rows if v == round(v) and v != 0]
    round_ratio = len(round_ints) / len(rows)
    if round_ratio > 0.4:
        issues.append(f"  ⚠️ {round_ratio:.0%} of values are integers (possible rounding)")

    # Repeat values
    counter = Counter(rows)
    repeats = {v: c for v, c in counter.items() if c > 3 and v != 0}
    if repeats:
        issues.append(f"  ⚠️ Repeated values: {repeats}")

    return issues


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', nargs='+', help='CSV data files')
    parser.add_argument('--tex', help='Main LaTeX file')
    parser.add_argument('--si', help='SI LaTeX file')
    args = parser.parse_args()

    print(f"\n{'='*55}")
    print(f"  Data Consistency Validation Report")
    print(f"{'='*55}")

    all_found = 0
    all_issues = []

    # Check CSV statistical fingerprints
    if args.csv:
        print(f"\n[CSV统计指纹检测]")
        for csv_path in args.csv:
            issues = check_csv_fingerprint(Path(csv_path))
            if issues:
                print(f"\n  {Path(csv_path).name}:")
                for i in issues:
                    print(f"  {i}")
                    all_issues.append(i)
            all_found += 1

    # Check tex numerical consistency
    if args.tex:
        print(f"\n[正文数值提取]")
        tex_nums = extract_tex_numbers(Path(args.tex))
        print(f"  Found: { {k: len(v) for k, v in tex_nums.items()} }")

        # Check R² range
        if 'r2' in tex_nums:
            for v in tex_nums['r2']:
                if v > 0.98:
                    all_issues.append(f"  ⚠️ R²={v:.3f} > 0.98 (suspiciously high)")
                elif v < 0.6:
                    all_issues.append(f"  ⚡ R²={v:.3f} < 0.6 (low)")

        # Check tail distribution
        all_numbers = []
        for key in tex_nums:
            all_numbers.extend(tex_nums[key])
        tail_issues = check_tail_distribution(all_numbers)
        if tail_issues:
            print(f"\n  尾数分布:")
            for i in tail_issues:
                print(f"  {i}")
                all_issues.append(i)

        # Check SI consistency
        if args.si:
            si_nums = extract_tex_numbers(Path(args.si))
            print(f"\n  SI数值: { {k: len(v) for k, v in si_nums.items()} }")
            for key in tex_nums:
                if key in si_nums:
                    main_set = set(round(v, 3) for v in tex_nums[key])
                    si_set = set(round(v, 3) for v in si_nums[key])
                    diff = main_set.symmetric_difference(si_set)
                    if diff:
                        all_issues.append(f"  ⚠️ {key} mismatch: main={main_set}, SI={si_set}")
                        print(f"  ⚠️ {key}: main={main_set}, SI={si_set}")

    # Summary
    print(f"\n{'─'*55}")
    if not all_issues:
        print(f"✅ All checks passed")
    else:
        print(f"Found {len(all_issues)} items to review:")
        for i in all_issues:
            print(f"  {i}")
    print(f"{'='*55}")


if __name__ == '__main__':
    main()
