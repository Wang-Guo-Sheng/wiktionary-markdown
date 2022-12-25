#!/usr/bin/python

from bs4 import BeautifulSoup
# import requests
import dryscrape

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

# using local kiwix wiktionary
baseurl = 'http://192.168.2.18:8081/viewer#wiktionary_en_all_maxi_2022-09/A/'
# baseurl = "https://en.wiktionary.org/wiki/"

url = baseurl + word

# r = requests.get(url)
# data = r.text
# print(data)

session = dryscrape.Session()
session.visit(my_url)
data = session.body()

soup = BeautifulSoup(data, features="lxml")
mpo = soup.find('div', id="mw-content-text")
try:
    # online wiktionary
    h = mpo.find('span', id=lang_id).parent
    outtext = str(h).replace(lang_id, word)
    while h:
        h = h.nextSibling
        if h is None:
            break
        if (h.name == "hr") or (h.name == "h2"):
            break
        outtext += str(h)
except AttributeError:
    try:
        # offline kiwix service
        h = ''.join(
            mpo.find('h2', id=lang_id).parent.find_next_siblings('details'))
        outtext = str(h).replace(lang_id, word)
    except AttributeError as exp:
        raise ValueError(
            "\"{}\" cannot be found in english wiktionary.".format(word)) from exp
except Exception:
    logging.error(traceback.format_exc())
else:
    print(outtext)
