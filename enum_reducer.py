#!/usr/bin/env python3
import sys

unique_id = 0
current_word = None

for line in sys.stdin:
    word = line.strip()
    if word != current_word:
        current_word = word
        print(f'{word}\t{unique_id}')
        unique_id += 1
