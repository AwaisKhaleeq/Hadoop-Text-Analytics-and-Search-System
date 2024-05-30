import sys

#!/usr/bin/env python3


articles = {}
word_enumerate = {}
word_freq = {}

for line in sys.stdin:
    line = line.strip()
    if line.startswith('*'):
        article_id, text = line[1:].split('\t', 1)
        articles[article_id] = text
    elif line.startswith('-'):
        word, word_id = line[1:].split('\t', 1)
        word_enumerate[word] = word_id

unique_words = set()
for text in articles.values():
    unique_words.update(text.split())

for word in unique_words:
    for text in articles.values():
        if word in text.split():
            word_freq[word] = word_freq.get(word, 0) + 1

with open('/home/saadali/hadoop/hadoop-2.10.2/i211659_SaadIbtasam/input.txt', 'w') as file:
    for article_id, text in articles.items():
        file.write(f"*{article_id}\t{text}\n")
    for word, freq in word_freq.items():
        if word in word_enumerate:
            word_id = word_enumerate[word]
            file.write(f"-{word}\t{freq}\t{word_id}\n")
