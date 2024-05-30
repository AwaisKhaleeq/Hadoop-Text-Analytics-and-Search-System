import sys
import re

#!/usr/bin/env python3

for line in sys.stdin:
    line = line.strip()
    doc_id, text = line.split('\t', 1)
    words = re.sub(r'\W+', ' ', text).lower().split()
    for word in words:
        print(f'{word}')
