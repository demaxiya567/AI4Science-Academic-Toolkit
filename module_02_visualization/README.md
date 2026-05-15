# Module 2: 可视化规范与工具

> **出版级科研图表的一站式规范与脚本**

## 核心理念

同一篇论文的所有图必须视觉统一。颜色、字体、尺寸、参考线风格从统一配置读取，各章节不各自hardcode。

## 包含内容

| 文件 | 用途 |
|------|------|
| `figure_style_standard.md` | 字体/AI痕迹/DPI/参考线的全局规范 |
| `visual_persuasion_checklist.md` | 视觉说服力快速检查 |
| `hyphen_dash_guide.md` | 英文论文连字符/en-dash/em-dash规范 |
| `decimal_precision_guide.md` | 小数精度与尾数分布规范 |
| `title_case_guide.md` | 论文标题大小写（journal-specific） |
| `drawio_convention.md` | draw.io源文件命名与导出规范 |
| `assets/color_palettes.py` | 色盲友好配色Python模块 |
| `assets/nature.mplstyle` | Nature风格matplotlib配置文件 |
| `assets/publication.mplstyle` | 通用出版风格matplotlib配置 |
| `assets/presentation.mplstyle` | 演示文稿风格matplotlib配置 |
| `assets/journal_requirements.md` | 各期刊图表尺寸要求速查 |
| `scripts/figure_export.py` | 多格式导出工具（PDF/PNG/SVG） |
| `scripts/style_presets.py` | 一键应用期刊风格的配置模块 |
| `scripts/figure_validator.py` | 图表技术验证（DPI/字体/尺寸/CJK） |

## 使用流程

```
Step 1: 安装依赖: pip install matplotlib numpy
Step 2: 复制 assets/color_palettes.py 和 scripts/style_presets.py 到项目目录
Step 3: 在绘图脚本中：
    from style_presets import configure_for_journal
    configure_for_journal('nature', figure_width='single')
    # ... 你的绘图代码 ...
    from figure_export import save_publication_figure
    save_publication_figure(fig, 'myfig', formats=['pdf', 'png'])
```

## 跨论文颜色一致性

同一方法跨论文的颜色必须一致。
在 `color_palettes.py` 中定义 `METHOD_COLORS` 字典，所有章节共享。
