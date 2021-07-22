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
    input_transcript = '/Users/ashisharora/Desktop/root/corpora/TDCorpus/analysis/topic_text'
    text_file_handle = open(input_transcript, 'r', encoding='utf8')
    text_file_data = text_file_handle.read().strip().split("\n")
    output_transcript = '/Users/ashisharora/Desktop/root/corpora/TDCorpus/analysis/secondary_topic_id'
    output_transcript_handle = open(output_transcript, 'w', encoding='utf8')
    primary_topic2duration = dict()
    secondary_topic2duration = dict()
    for line in text_file_data:
        parts = line.strip().split()
        if len(parts) == 4:
            topic = parts[2]
            # topic = parts[2].split('-')[0]
            topic_type = parts[3]
            topic_type = topic_type.strip().split()[0]

            if topic not in primary_topic2duration:
                primary_topic2duration[topic] = 0
            if topic not in secondary_topic2duration:
                secondary_topic2duration[topic] = 0

            if topic_type == 'p':
                primary_topic2duration[topic] += 1
            else:
                secondary_topic2duration[topic]+= 1
                output_transcript_handle.write(topic + '\n')
    
    # for key in sorted(secondary_topic2duration):
    #     output_str = str(key) + " " + str(secondary_topic2duration[key])
    #     print(output_str)

if __name__ == '__main__':
    main()