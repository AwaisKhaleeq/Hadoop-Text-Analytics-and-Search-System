#!/usr/bin/env python3

import sys

word_count_id = {}
unique_words = []
query = ""
idf_vectors = {}

for line in sys.stdin:
    line = line.strip()
    if line.startswith('+'):
        key, value = line[1:].split('\t')  # Remove the "+" and split the line
        value_list = eval(value)
        idf_vectors[key] = value_list
    elif line.startswith('-'):
        parts = line[1:].split('\t')  # Remove the "-" and split the line
        word_count_id[parts[0]] = [parts[1], parts[2]]
    elif line.startswith('*'):
        query = line[1:].strip()  # Remove the "*" and any leading/trailing whitespace
        words = query.split(' ')
        for word in words:
            if word not in unique_words:
                unique_words.append(word)

word_ids = {}
for word in unique_words:
    if word in word_count_id:
        word_ids[word] = word_count_id[word][1]
        
tf = {}
for word in query.split(' '):
    if word not in tf:
        tf[word]=1
    else:
        tf[word]+=1
        
idf = {}
for key, value in tf.items():
    if key in word_count_id:
        idf[key]=tf[key]/int(word_count_id[key][0])
        
idf_updated = {}
for word, idf in idf.items():
    if word in word_count_id:
        idf_updated[word_count_id[word][1]] = idf
        
query_vector = [0] * int(len(word_count_id))


for i in range(0,len(word_count_id)-1):
    if str(i) in idf_updated:
        query_vector[i] = idf_updated[str(i)]
        
        
def inner_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same length")

    result = 0
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]

    return result


for document, vector in idf_vectors.items():
    print(f"Document {document} : {inner_product(vector,query_vector)}")