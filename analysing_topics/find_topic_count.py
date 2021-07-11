#!/usr/bin/env python3

import os
import argparse
# parser = argparse.ArgumentParser(description="""get text from transcripts""")
# parser.add_argument('input_transcript', type=str, help='File name of a file that contains the')
# parser.add_argument('output_transcript', type=str, help='Output file that contains transcript')
def main():

    # args = parser.parse_args()
    # output_transcript_handle = open(args.output_transcript, 'w', encoding='utf8')
    # text_file_handle = open(args.input_transcript, 'r', encoding='utf8')
    input_transcript = '/Users/ashisharora/Desktop/root/corpora/TDCorpus/topic2/topic_text'
    text_file_handle = open(input_transcript, 'r', encoding='utf8')
    text_file_data = text_file_handle.read().strip().split("\n")
    topic2duration = dict()
    for line in text_file_data:
        parts = line.strip().split()
        if len(parts) == 4:
            topic = parts[2].split('-')[0]
            if topic not in topic2duration:
                topic2duration[topic] = 0
            topic2duration[topic] += 1
    
    for key in sorted(topic2duration):
        output_str = str(key) + " " + str(topic2duration[key])
        print(output_str)

if __name__ == '__main__':
    main()