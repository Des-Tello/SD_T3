#!/usr/bin/env python
# -*-coding:utf-8 -*

import sys
import re

for line in sys.stdin:
    docs = line.lower()
    for char in [",", ".", '"', "'", "(", ")", "\\", ";", ":", "$1", "$", "&"]:
        docs = docs.replace(char, '')

    docs = docs.split('<end>')[0:-1]

    for i,words in enumerate(docs):
        for word in words.split():
            print('{}\t{}\t{}'.format(word, i+1, 1))