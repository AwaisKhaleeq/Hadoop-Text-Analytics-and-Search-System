import sys
from collections import defaultdict

#!/usr/bin/env python3

current_doc_id = None
term_counts = defaultdict(int)

# Read input from stdin
for line in sys.stdin:
    doc_id, word, count = line.strip().split('\t', 1)
    count = int(count)
    
    # Check if the document ID is the same as the previous one
    if doc_id == current_doc_id:
        term_counts[word] += count
    else:
        # If it's a new document ID, print the term counts for the previous document
        if current_doc_id:
            for word, count in term_counts.items():
                print(f'{current_doc_id}\t{word}\t{count}')
        
        # Update the current document ID and reset the term counts
        current_doc_id = doc_id
        term_counts = defaultdict(int)
        term_counts[word] = count

# Output the term counts for the last document
if current_doc_id:
    for word, count in term_counts.items():
        print(f'{current_doc_id}\t{word}\t{count}')
