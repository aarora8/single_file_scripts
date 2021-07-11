#!/usr/bin/env python3

import os
import argparse
from datetime import datetime
from datetime import timedelta
# parser = argparse.ArgumentParser(description="""get text from transcripts""")
# parser.add_argument('input_transcript', type=str, help='File name of a file that contains the')
# parser.add_argument('output_transcript', type=str, help='Output file that contains transcript')
def main():

    # args = parser.parse_args()
    # output_transcript_handle = open(args.output_transcript, 'w', encoding='utf8')
    # text_file_handle = open(args.input_transcript, 'r', encoding='utf8')
    output_transcript = '/Users/ashisharora/Desktop/root/corpora/TDCorpus/analysis/topic_duration'
    input_transcript = '/Users/ashisharora/Desktop/root/corpora/TDCorpus/analysis/topic_text'
    output_transcript_handle = open(output_transcript, 'w', encoding='utf8')
    text_file_handle = open(input_transcript, 'r', encoding='utf8')
    text_file_data = text_file_handle.read().strip().split("\n")
    topic2duration = dict()
    primarynsecondary = dict()
    for line in text_file_data:
        parts = line.strip().split()
        if len(parts) == 4:
            topic = parts[2].split('-')[0]
            if topic not in topic2duration:
                topic2duration[topic] = datetime.strptime('00:0', '%M:%S')
            start_seconds_txt = parts[0].strip().split('.')[0]
            end_seconds_txt = parts[1].strip().split('.')[0]
            if ':' in parts[0]:
                start_seconds = datetime.strptime(start_seconds_txt, '%M:%S')
                end_seconds = datetime.strptime(end_seconds_txt, '%M:%S')
            else:
                start_seconds = timedelta(seconds=int(start_seconds_txt))
                end_seconds = timedelta(seconds=int(end_seconds_txt))
            assert end_seconds >= start_seconds
            diff = end_seconds - start_seconds
            topic2duration[topic] += diff
    
    for key in sorted(topic2duration):
        output_str = str(key) + " " + str(topic2duration[key]).split(" ")[1]
        output_transcript_handle.write(output_str + '\n')
        # print(output_str)


if __name__ == '__main__':
    main()