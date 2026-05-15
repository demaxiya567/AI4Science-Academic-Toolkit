#!/usr/bin/env python3
"""
DOI → BibTeX converter via Crossref API.

Usage:
    python doi_to_bibtex.py --dois "10.1016/j.cattod.2023.01" "10.1021/acscatal.3c01234"
    python doi_to_bibtex.py --file doids.txt
    python doi_to_bibtex.py --bib refs.bib (extract DOIs from existing bib)
"""

import re
import sys
import json
import argparse
import urllib.request
import urllib.parse
from pathlib import Path


CROSSREF_API = "https://api.crossref.org/works/"


def doi_to_bibtex(doi):
    """Convert a single DOI to BibTeX via Crossref API."""
    url = CROSSREF_API + urllib.parse.quote(doi)
    headers = {
        'User-Agent': 'CitationTool/1.0 (mailto:example@example.com)',
        'Accept': 'application/json',
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            return parse_crossref_response(data, doi)
    except Exception as e:
        return f"% Error fetching {doi}: {e}"


def parse_crossref_response(data, doi):
    """Parse Crossref JSON response into BibTeX entry."""
    msg = data.get('message', {})
    title = msg.get('title', ['Unknown'])[0]
    authors = msg.get('author', [])
    year = msg.get('published-print', {}).get('date-parts', [[None]])[0][0]
    if not year:
        year = msg.get('published-online', {}).get('date-parts', [[None]])[0][0]
    journal = msg.get('container-title', ['Unknown'])[0]
    volume = msg.get('volume', '')
    issue = msg.get('issue', '')
    pages = msg.get('page', '')
    publisher = msg.get('publisher', '')

    # Generate cite key
    first_author = authors[0]['family'] if authors else 'Unknown'
    cite_key = f"{first_author}{year}"

    # Build entry
    entry = f"@article{{{cite_key},\n"
    entry += f"  author = {{{' and '.join(a['family'] + ', ' + a.get('given', '') for a in authors[:10])}}},\n"
    if len(authors) > 10:
        entry += f"  author = {{{' and '.join(a['family'] + ', ' + a.get('given', '') for a in authors[:10])} and others}},\n"
    entry += f"  title = {{{title}}},\n"
    entry += f"  journal = {{{journal}}},\n"
    entry += f"  year = {{{year}}},\n"
    if volume:
        entry += f"  volume = {{{volume}}},\n"
    if issue:
        entry += f"  number = {{{issue}}},\n"
    if pages:
        entry += f"  pages = {{{pages}}},\n"
    entry += f"  doi = {{{doi}}}\n"
    entry += "}\n"
    return entry


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dois', nargs='+', help='DOIs to convert')
    parser.add_argument('--file', help='File with one DOI per line')
    parser.add_argument('--output', default='-', help='Output file (default: stdout)')
    args = parser.parse_args()

    dois = []
    if args.dois:
        dois.extend(args.dois)
    if args.file:
        with open(args.file) as f:
            dois.extend(line.strip() for line in f if line.strip())

    if not dois:
        print("No DOIs provided.")
        sys.exit(1)

    entries = []
    for doi in dois:
        print(f"Fetching {doi}...", file=sys.stderr)
        entry = doi_to_bibtex(doi)
        entries.append(entry)

    output = '\n'.join(entries)
    if args.output == '-':
        print(output)
    else:
        Path(args.output).write_text(output, encoding='utf-8')
        print(f"Written to {args.output}")


if __name__ == '__main__':
    main()
