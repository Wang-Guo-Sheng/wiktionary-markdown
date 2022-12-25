#!/usr/bin/python

from bs4 import BeautifulSoup
import requests

import argparse

import traceback
import logging

import sys
sys.tracebacklimit = 0

parser = argparse.ArgumentParser(prog='wiktdl',
                                 description='Extract word definition in a specified language from english wiktionary',
                                 epilog='Usage: wiktdl <word> <Language>')
parser.add_argument('word', type=str, nargs=1)
parser.add_argument('Language', type=str, nargs=1)

args = parser.parse_args()
word = args.word[0]
lang_id = args.Language[0]

baseurl = "https://en.wiktionary.org/wiki/"
url = baseurl + word

r = requests.get(url)
data = r.text

soup = BeautifulSoup(data, features="lxml")
mpo = soup.find('div', {"class": "mw-parser-output"})
try:
    h = mpo.find('span', id=lang_id).parent
    outtext = str(h).replace(lang_id, word)
    while h:
        h = h.nextSibling
        if h is None:
            break
        if (h.name == "hr") or (h.name == "h2"):
            break
        outtext += str(h)
except AttributeError as exp:
    raise ValueError(
        "\"{}\" cannot be found in english wiktionary.".format(word)) from exp
except Exception:
    logging.error(traceback.format_exc())
else:
    print(outtext)
