#!/usr/bin/python

import argparse
import re

parser = argparse.ArgumentParser(prog='multiline_brackets',
                                 description='Remove newlines within square brackets',
                                 epilog='Usage: multiline_brackets <file>')
parser.add_argument('file', type=str, nargs=1)
args = parser.parse_args()
file = args.file[0]

with open(file, 'r') as f:
    data = "".join(f.readlines())
    data = re.sub(r"(\[[^\]]*)\n([^\[\]]*\n)*([^\[]*\])",
                  lambda m: " ".join([g.replace('\n', '') for g in m.groups() if g is not None]), data)

with open(file, 'w') as f:
    f.write(data)
