#!/usr/bin/env python3
"""
Citation Validator — check citation existence via DOI/Crossref.

Usage:
    python validate_citations.py --bib refs.bib
    python validate_citations.py --dois "10.1016/..." "10.1021/..."
"""

import re
import argparse
from pathlib import Path
from doi_to_bibtex import CROSSREF_API


def check_doi_exists(doi):
    """Quick check if a DOI is resolvable."""
    import urllib.request
    url = f"https://doi.org/{doi}"
    try:
        req = urllib.request.Request(url, method='HEAD')
        # Use a shorter timeout — we just want existence check
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status == 200
    except Exception:
        return False


def extract_dois_from_bib(bib_path):
    """Extract DOIs from a bib file."""
    content = Path(bib_path).read_text(encoding='utf-8', errors='ignore')
    dois = re.findall(r'doi\s*=\s*[{"]?(10\.\S+?)[}"]', content, re.IGNORECASE)
    return dois


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bib', help='BibTeX file')
    parser.add_argument('--dois', nargs='+', help='DOIs to check directly')
    args = parser.parse_args()

    dois = []
    if args.bib:
        dois = extract_dois_from_bib(Path(args.bib))
        print(f"Extracted {len(dois)} DOIs from {args.bib}")
    if args.dois:
        dois.extend(args.dois)

    if not dois:
        print("No DOIs provided.")
        return

    valid = 0
    invalid = 0
    for doi in dois[:30]:  # Limit to 30 to avoid timeout
        exists = check_doi_exists(doi)
        if exists:
            valid += 1
        else:
            print(f"⚠️  DOI not resolvable: {doi}")
            invalid += 1

    print(f"\nChecked: {valid+invalid}, Valid: {valid}, Suspicious: {invalid}")


if __name__ == '__main__':
    main()
