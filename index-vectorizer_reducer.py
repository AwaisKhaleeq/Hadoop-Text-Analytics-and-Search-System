#!/usr/bin/env python3
data_dict = {}

import sys

for line in sys.stdin:
    if line.startswith('*'):
        # Split the line at the tab characte
        key, values = line.strip().split('\t',1)
        print(f"{key}\t{values}")
        items = values.split()
        
        # Convert each item into a tuple and add it to the list
        data_list = [tuple(map(lambda x: float(x.strip('()')), item.split(','))) for item in items]
                        
        # Store the data in the dictionary
        data_dict[key] = data_list
    if line.startswith('-'):
        num = line.strip()
        num = num[1:]

idf_vectors = {}
for docs, idf in data_dict.items():
    empty_list = [0] * int(num)
    for value in idf:
        empty_list[int(value[0])] = value[1]
    idf_vectors[docs]=empty_list
    

with open("/home/hadoopuser/i211377_A2/idf_vectors.txt", "w") as file:
    for key, values in idf_vectors.items():
        # Convert the list of values to a string enclosed in square brackets
        values_str = "[" + ", ".join(map(str, values)) + "]"
        
        # Write key and values to the file
        key = key[1:]
        file.write(f"{key}\t{values_str}\n")