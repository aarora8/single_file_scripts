#!/usr/bin/env python3

import os
import argparse
import glob
# parser = argparse.ArgumentParser(description="""get text from transcripts""")
# parser.add_argument('input_transcript', type=str, help='File name of a file that contains the'
#                     'text. Each line must be: <uttid> <word1> <word2> ...')
# parser.add_argument('output_transcript', type=str, help='Output file that contains transcript')
def main():

    # args = parser.parse_args()
    # input_transcript = '/Users/ashisharora/Desktop/root/corpora/TDCorpus/topic_text'
    # text_file_handle = open(input_transcript, 'r', encoding='utf8')
    # text_file_data = text_file_handle.read().strip().split("\n")
    list_of_files = glob.glob('/Users/ashisharora/Desktop/root/corpora/TDCorpus/topics/*.txt')
    output_transcript = '/Users/ashisharora/Desktop/root/corpora/TDCorpus/topic_text'
    output_transcript_handle = open(output_transcript, 'w', encoding='utf8')
    for file_name in list_of_files:
        text_file_handle = open(file_name, 'r', encoding='utf8')
        text_file_data = text_file_handle.read().strip().split("\n")
        for line in text_file_data:
            parts = line.strip().split("\n")
            output_transcript_handle.write(" ".join(parts) + '\n')


if __name__ == '__main__':
    main()