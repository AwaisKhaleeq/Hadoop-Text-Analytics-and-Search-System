#!/usr/bin/env python3

import sys

articles = {}
word_enumerate = {}

for line in sys.stdin:
    line = line.strip()
    if line.startswith('*'):
        article_id, text = line.split('\t', 1)
        print(f"{article_id}\t{text}")
    elif line.startswith('-'):
        word, id = line.split('\t', 1)
        print(f"{word}\t{id}")