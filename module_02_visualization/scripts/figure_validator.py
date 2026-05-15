#!/usr/bin/env python3
"""
Figure Validation Pipeline — programmatic verification of all figures.

Usage:
    python figure_validator.py path/to/figures/
    python figure_validator.py --script plot_fig1.py
"""

import subprocess
import sys
from pathlib import Path
from PIL import Image


def check_image_size(image_path: Path):
    """Check image dimensions and DPI."""
    img = Image.open(image_path)
    dpi = img.info.get('dpi', (72, 72))
    return {
        'path': str(image_path),
        'size': img.size,
        'dpi': dpi[0],
        'format': img.format,
    }


def check_pdf_fonts(pdf_path: Path):
    """Check for Type3 fonts in PDF (type3 = rendering issues)."""
    result = subprocess.run(
        ['pdffonts', str(pdf_path)],
        capture_output=True, text=True, timeout=10
    )
    has_type3 = 'Type 3' in result.stdout
    return {
        'path': str(pdf_path),
        'type3_fonts': has_type3,
        'fonts_detail': result.stdout[:500] if result.stdout else 'pdffonts not available'
    }


def check_cjk_mathmode(script_path: Path):
    """Check for Chinese characters inside math mode."""
    content = script_path.read_text(encoding='utf-8', errors='ignore')
    import re
    # Find $...$ patterns containing CJK characters
    math_mode = re.findall(r'\$(.+?)\$', content)
    issues = []
    for mm in math_mode:
        for char in mm:
            if '一' <= char <= '鿿':
                issues.append(f"  CJK in math mode: '${mm}$'")
                break
    return issues


def validate_all(figures_dir: Path):
    results = []
    for f in sorted(figures_dir.glob('*')):
        if f.suffix.lower() in ('.png', '.jpg', '.tiff', '.tif'):
            info = check_image_size(f)
            if info['dpi'] < 300:
                print(f"⚠️  {f.name}: DPI={info['dpi']} < 300")
            else:
                print(f"✅ {f.name}: {info['size']}, DPI={info['dpi']}")
            results.append(info)

        elif f.suffix.lower() == '.pdf':
            font_info = check_pdf_fonts(f)
            status = '⚠️ Type3' if font_info['type3_fonts'] else '✅'
            print(f"{status} {f.name}")
            results.append(font_info)

    print(f"\nChecked {len(results)} files in {figures_dir}")
    return results


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python figure_validator.py <figures_dir/>  — batch check all images")
        print("  python figure_validator.py --script <file.py>  — check script for CJK issues")
        sys.exit(1)

    path = Path(sys.argv[1])

    if sys.argv[1] == '--script' and len(sys.argv) > 2:
        script = Path(sys.argv[2])
        issues = check_cjk_mathmode(script)
        if issues:
            print(f"⚠️  Found {len(issues)} CJK-in-math-mode issues in {script.name}:")
            for i in issues:
                print(i)
        else:
            print(f"✅ {script.name}: No CJK-in-math-mode issues")
    else:
        validate_all(path)
