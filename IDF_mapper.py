import sys
import re

#!/usr/bin/env python3

def mapper():
    for line in sys.stdin:
        try:
            line = line.strip()
            doc_id, text = line.split('\t', 1)
            words = re.findall(r'\b\w+\b', text.lower())
            for word in words:
                print(f'{doc_id}\t{word}\t1')
        except ValueError as e:
            # Optionally log to stderr for debugging
            print(f"reporter:counter:Mapper Counters,Errors,1", file=sys.stderr)
            continue

if __name__ == "__main__":
    mapper()
