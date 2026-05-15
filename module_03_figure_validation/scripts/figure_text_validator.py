#!/usr/bin/env python3
"""
Figure-Text Validator: cross-validate numerical values between Python scripts,
LaTeX captions, and in-text references.

Usage:
    python figure_text_validator.py --scripts figures/*.py --tex main.tex
    python figure_text_validator.py --tex main.tex --si SI.tex
"""

import re
import sys
import argparse
from pathlib import Path


def extract_script_values(py_path):
    """Extract numeric values and annotations from Python plotting scripts."""
    content = Path(py_path).read_text(encoding='utf-8', errors='ignore')
    values = {
        'r2': re.findall(r"[Rr][²\^]?2\s*[=:]\s*([\d.]+)", content),
        'mae': re.findall(r"MAE\s*[=:]\s*([\d.]+)", content, re.IGNORECASE),
        'rmse': re.findall(r"RMSE\s*[=:]\s*([\d.]+)", content, re.IGNORECASE),
        'savefig': re.findall(r"savefig\(['\"](.+?)['\"]", content),
        'xlabel': re.findall(r"set_xlabel\(['\"](.+?)['\"]", content),
        'ylabel': re.findall(r"set_ylabel\(['\"](.+?)['\"]", content),
        'annotations': re.findall(r"annotate\(['\"](.+?)['\"]", content),
    }
    return values


def extract_tex_figures(tex_path):
    """Extract figure-related info from LaTeX files."""
    content = Path(tex_path).read_text(encoding='utf-8', errors='ignore')
    figures = {
        'captions': re.findall(r'\\caption\{(.+?)\}', content, re.DOTALL),
        'includes': re.findall(r'\\includegraphics.*?\{(.+?)\}', content),
        'labels': re.findall(r'\\label\{(fig:.+?)\}', content),
        'refs': re.findall(r'(?:Figure|Fig\.?)\s*\\ref\{(fig:.+?)\}', content),
    }
    # Extract numbers from captions
    figures['numerical_claims'] = re.findall(
        r'R[²\^]?2\s*[=≈]\s*([\d.]+)', content
    )
    return figures


def compare_values(tex_path, script_paths):
    print(f"\n{'='*55}")
    print(f"  Figure-Text Validation Report")
    print(f"{'='*55}")

    tex_figures = extract_tex_figures(tex_path)

    # Check caption-image count
    script_includes = []
    for sp in script_paths:
        sv = extract_script_values(sp)
        for sg in sv['savefig']:
            script_includes.append(sg)

    print(f"\n  Files: main={tex_path.name}, scripts={len(script_paths)}")
    print(f"  Captions: {len(tex_figures['captions'])}")
    print(f"  Images referenced in LaTeX: {len(tex_figures['includes'])}")
    print(f"  Images from scripts: {len(script_includes)}")

    # Check for missing image references
    tex_images = set(tex_figures['includes'])
    script_images = set(script_includes)
    missing_refs = script_images - tex_images
    if missing_refs:
        print(f"\n⚠️  Images generated but not referenced in LaTeX:")
        for m in missing_refs:
            print(f"   - {m}")

    # Check R² consistency
    caption_r2 = set(tex_figures['numerical_claims'])
    all_script_r2 = set()
    for sp in script_paths:
        sv = extract_script_values(sp)
        all_script_r2.update(sv['r2'])

    if caption_r2 and all_script_r2:
        diff = caption_r2.symmetric_difference(all_script_r2)
        if diff:
            print(f"\n⚠️  R² value mismatch between caption and scripts:")
            print(f"   Caption has: {caption_r2}")
            print(f"   Scripts have: {all_script_r2}")
        else:
            print(f"\n✅ R² values consistent between caption and scripts")

    print(f"\n{'='*55}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--tex', required=True, help='Main LaTeX file')
    parser.add_argument('--scripts', nargs='+', help='Python figure scripts')
    args = parser.parse_args()

    if not args.scripts:
        print("No scripts specified; extracting figures from LaTeX only.")
        print("Use: --scripts to specify Python figure scripts.")

    script_paths = [Path(s) for s in (args.scripts or [])]
    compare_values(Path(args.tex), script_paths)
