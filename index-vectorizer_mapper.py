#!/usr/bin/env python3
import sys

for line in sys.stdin:
    if line.startswith('*'):
        # Split the line at the tab character
        key, values = line.strip().split('\t',1)
        print(f"{key}\t{values}")
    if line.startswith('-'):
        num = line.strip()
        print(num)