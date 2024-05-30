#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()  # Remove leading and trailing whitespace
    if line:  # Check if the line is not empty after stripping whitespace
        print(line)