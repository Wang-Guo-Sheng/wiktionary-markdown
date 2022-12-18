#!/usr/bin/python

import argparse
import re

parser = argparse.ArgumentParser(prog='compact_etym',
                                 description='Remove line breaks in etymology sections',
                                 epilog='Usage: compact_etym.py <file>')
parser.add_argument('file', type=str, nargs=1)
args = parser.parse_args()
file = args.file[0]

with open(file, 'r') as f:
  data = "".join(f.readlines())
  data = re.sub(r"###\s*Etymology((\n([^#]+#)*[^#]*)*)\n#",
                # lambda m: print(m),
                lambda m: "### Etymology\n" +
                m.group(1).replace('\n', ' ') + "\n#",
                data)
  data = re.sub(r"####\s*Derived\s[Tt]erms((\n([^#]+#)*[^#]*)*)\n#",
                # lambda m: print(m),
                lambda m: "#### Derived terms\n" + \
                re.sub(r'^\,\s*', '',
                       m.group(1).replace('\n-', ', ').replace('\n', '')
                       ) + "\n#",
                data)
  data = re.sub(r"####\s*Descendants((\n([^#]+#)*[^#]*)*)\n#",
                # lambda m: print(m),
                lambda m: "#### Descendants\n" + \
                re.sub(r'^\,\s*', '',
                       m.group(1).replace('\n-', ', ').replace('\n', '')
                       ) + "\n#",
                data)

with open(file, 'w') as f:
  f.write(data)
