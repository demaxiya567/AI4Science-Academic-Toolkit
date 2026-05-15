#!/usr/bin/env python3
"""
Cross-Reference Checker: verify all \ref, \cite, \includegraphics consistency.

Usage:
    python cross_ref_checker.py --tex main.tex --bib refs.bib
    python cross_ref_checker.py --tex-dir ./chapters/ --bib refs.bib
"""

import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict


def scan_tex_files(paths):
    """Scan .tex files for all reference elements."""
    labels = set()       # defined \label{xxx}
    refs = defaultdict(list)     # \ref{xxx} -> [file:line]
    cites = defaultdict(list)    # \cite{xxx} -> [file:line]
    includes = []        # \includegraphics{xxx}
    eq_labels = set()    # \label{eq:xxx}
    fig_labels = set()   # \label{fig:xxx}
    tab_labels = set()   # \label{tab:xxx}

    for tex_path in paths:
        content = tex_path.read_text(encoding='utf-8', errors='ignore')
        lines = content.split('\n')
        fname = tex_path.name

        for lineno, line in enumerate(lines, 1):
            # Find \label
            for m in re.finditer(r'\\label\{([^}]+)\}', line):
                labels.add(m.group(1))
                if m.group(1).startswith('fig:'):
                    fig_labels.add(m.group(1))
                elif m.group(1).startswith('tab:'):
                    tab_labels.add(m.group(1))
                elif m.group(1).startswith('eq:'):
                    eq_labels.add(m.group(1))

            # Find \ref (non-cite)
            for m in re.finditer(r'\\ref\{([^}]+)\}', line):
                refs[m.group(1)].append(f'{fname}:{lineno}')

            # Find \cite variations
            for m in re.finditer(r'\\citet?e?p?\*?\{([^}]+)\}', line):
                keys = m.group(1).split(',')
                for k in keys:
                    cites[k.strip()].append(f'{fname}:{lineno}')

            # Find \includegraphics
            for m in re.finditer(r'\\includegraphics(?:\[.*?\])?\{([^}]+)\}', line):
                includes.append(f'{m.group(1)} ({fname}:{lineno})')

    return {
        'labels': labels, 'refs': refs, 'cites': cites,
        'includes': includes,
        'fig_labels': fig_labels, 'tab_labels': tab_labels, 'eq_labels': eq_labels,
    }


def scan_bib(bib_path):
    """Scan .bib file for all entry keys."""
    content = bib_path.read_text(encoding='utf-8', errors='ignore')
    keys = set(re.findall(r'@\w+\{([^,]+),', content))
    return keys


def report(tex_results, bib_keys=None):
    print(f"\n{'='*55}")
    print(f"  Cross-Reference Check Report")
    print(f"{'='*55}")

    issues = []

    # Check \ref -> \label
    for ref_key, locations in tex_results['refs'].items():
        if ref_key not in tex_results['labels']:
            issues.append(f"🔴 BROKEN REF: '{ref_key}' at {locations[0]} — no matching \\label")

    # Check \cite -> .bib
    if bib_keys is not None:
        for cite_key, locations in tex_results['cites'].items():
            if cite_key not in bib_keys:
                issues.append(f"🔴 BROKEN CITE: '{cite_key}' at {locations[0]} — not in .bib")

        # Check unused bib entries
        used_cites = set(tex_results['cites'].keys())
        unused = bib_keys - used_cites
        if unused:
            print(f"\nℹ️  Unused bib entries ({len(unused)}):")
            for k in sorted(unused)[:10]:
                print(f"   - {k}")
            if len(unused) > 10:
                print(f"   ... and {len(unused)-10} more")

    # Report
    if not issues:
        print("\n✅ All references valid")
    else:
        print(f"\nIssues found: {len(issues)}")
        for issue in issues:
            print(f"  {issue}")

    # Summary
    print(f"\n  Labels: {len(tex_results['labels'])} defined")
    print(f"  Refs: {len(tex_results['refs'])} unique keys used")
    print(f"  Cites: {len(tex_results['cites'])} unique keys used")
    print(f"  Graphics: {len(tex_results['includes'])} \\includegraphics")
    print(f"{'='*55}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--tex', nargs='+', required=True, help='.tex files to check')
    parser.add_argument('--bib', help='.bib file to validate citations')
    parser.add_argument('--tex-dir', help='Directory with .tex files (alternative)')
    args = parser.parse_args()

    tex_paths = []
    if args.tex_dir:
        tex_paths = list(Path(args.tex_dir).glob('*.tex'))
    elif args.tex:
        tex_paths = [Path(t) for t in args.tex]

    if not tex_paths:
        print("No .tex files found.")
        sys.exit(1)

    results = scan_tex_files(tex_paths)

    bib_keys = None
    if args.bib:
        bib_keys = scan_bib(Path(args.bib))

    report(results, bib_keys)
