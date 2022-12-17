#!/usr/bin/python

import argparse
import re

parser = argparse.ArgumentParser(prog='internal_links',
                                 description='Convert wiktionary internal links to markdown internal links',
                                 epilog='Usage: internal_links.py <file>')
parser.add_argument('file', type=str, nargs=1)
args = parser.parse_args()
file = args.file[0]

with open(file, 'r') as f:
    data = "".join(f.readlines())
    data = re.sub(r'\[([^\]]*)\]\(([^\)]*("[^"]*"))\)',
                  lambda m: '[' + m.group(1) + ']' + '(' + m.group(2) + ')'
                  if m.group(2)[:4] == 'http' else ('[[' + m.group(1) + ']]'),
                  data)

with open(file, 'w') as f:
    f.write(data)
