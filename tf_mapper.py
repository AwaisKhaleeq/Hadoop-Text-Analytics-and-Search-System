import sys
import re

# Read input from standard input
for line in sys.stdin:
    line = line.strip()
    doc_id, text = line.split('\t', 1)
    
    # Remove non-alphanumeric characters and convert to lowercase
    words = re.sub(r'\W+', ' ', text).lower().split()
    
    # Output each word with its corresponding document ID and count
    for word in words:
        print(f'{doc_id}\t{word}\t1')
