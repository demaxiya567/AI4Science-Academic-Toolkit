# Journal-Specific Figure Requirements

Quick reference for common journal figure formatting requirements.

## Column Widths

| Journal | Single Column | 1.5 Column | Double Column |
|---------|--------------|------------|---------------|
| Nature / Nature series | 89 mm (3.5") | 114 mm (4.5") | 183 mm (7.2") |
| Science | 55 mm (2.2") | — | 175 mm (6.9") |
| Cell | 85 mm (3.35") | 114 mm (4.5") | 178 mm (7.0") |
| ACS journals | 84 mm (3.3") | — | 176 mm (6.93") |
| RSC journals | 84 mm (3.3") | — | 173 mm (6.81") |
| Elsevier journals | 90 mm (3.54") | 140 mm (5.51") | 190 mm (7.48") |
| MDPI journals | 85 mm (3.35") | — | 174 mm (6.85") |

## Format Requirements

| Journal | Preferred Format | DPI | Color Mode |
|---------|-----------------|-----|------------|
| Nature | Vector (PDF/EPS) | 300+ | RGB |
| Science | Vector (PDF/EPS) | 300+ | RGB |
| Cell | TIFF/EPS/PDF | 300+ | CMYK |
| ACS | TIFF/PDF/EPS | 300+ (600 for line art) | RGB |
| RSC | TIFF/EPS/PDF | 300+ | RGB |
| Elsevier | TIFF/EPS/PDF | 300+ | RGB/CMYK |
| MDPI | TIFF/JPG/PNG/EPS | 300+ | RGB |

## Font Guidelines

| Requirement | Specification |
|------------|--------------|
| Font family | Sans-serif (Arial, Helvetica) for most journals |
| Min font size | 6-7 pt at final print size |
| Axis labels | 7-9 pt |
| Panel labels | 8-12 pt, bold |
| Line weights | 0.5-2 pt (visible at final size) |

## Color Guidelines

| Requirement | Specification |
|------------|--------------|
| Colorblind-friendly | Required by most top journals |
| Never use | `jet` or `rainbow` colormaps |
| Recommended | `viridis`, `plasma`, `cividis` |
| For diverging data | `RdBu`, `PuOr`, `BrBG` (not RdGn) |

## Quick Matplotlib Setup

```python
import matplotlib.pyplot as plt

# For Nature single-column figure
plt.rcParams['figure.figsize'] = (3.5, 2.5)  # 89 mm
plt.rcParams['font.size'] = 8
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.labelsize'] = 9
plt.rcParams['xtick.labelsize'] = 7
plt.rcParams['ytick.labelsize'] = 7
plt.rcParams['lines.linewidth'] = 1.0
plt.rcParams['axes.linewidth'] = 0.5
```

> For automated journal configuration, use `scripts/style_presets.py`.
