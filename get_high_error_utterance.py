#!/usr/bin/env python3
# This script sorts the utterance based in the error
from collections import OrderedDict
import sys, io
import string
infile = '/Users/ashisharora/Desktop/per_utt.txt'
output = '/Users/ashisharora/Desktop/output.txt'
output_handle = open(output, 'w', encoding='utf8')
total_words = 0
total_error = 0
total_substitution = 0
total_insert = 0
total_deletion = 0
csid_dict = {}

for line in open(infile):
    line = line.strip().split(" ")
    
    utt_id = line[0]
    # get only csid lines
    if "csid" not in line[1]:
        continue

    correct = int(line[2])
    substitute = int(line[3])
    insert = int(line[4])
    delete = int(line[5])

    total_words = total_words + correct + substitute + delete
    total_error = total_error + substitute + delete + insert
    total_substitution = total_substitution + substitute
    total_insert = total_insert + insert
    total_deletion = total_deletion + delete
    csid_list = [correct, substitute, insert, delete]
    csid_dict[utt_id] = csid_list


# print(total_words)
# print(total_error)

precent_ins = total_insert * 100 / total_words
percent_del = total_deletion * 100 / total_words
percent_sub = total_substitution * 100 / total_words
wer = total_error * 100 / total_words

# print(total_insert)
# print(total_deletion)
# print(total_substitution)
# print("{:.2f}".format(wer))
for w in sorted(csid_dict.items(), key=lambda x: x[1][1], reverse=True):
    output_handle.write(str(w[0]) + ' ' + str(w[1]) + '\n')
