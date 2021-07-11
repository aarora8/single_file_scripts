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
    output_transcript = '/Users/ashisharora/Desktop/root/corpora/TDCorpus/analysis/topic_duration_secondary'
    input_transcript = '/Users/ashisharora/Desktop/root/corpora/TDCorpus/analysis/topic_text'
    output_transcript_handle = open(output_transcript, 'w', encoding='utf8')
    text_file_handle = open(input_transcript, 'r', encoding='utf8')
    text_file_data = text_file_handle.read().strip().split("\n")
    primary_topic2duration = dict()
    secondary_topic2duration = dict()
    for line in text_file_data:
        parts = line.strip().split()
        if len(parts) == 4:
            # topic = parts[2].split('-')[0]
            topic_type = parts[3]
            topic_type = topic_type.strip().split()[0]
            print(topic_type)
            topic = parts[2]
            
            
            start_seconds_txt = parts[0].strip().split('.')[0]
            end_seconds_txt = parts[1].strip().split('.')[0]
            if ':' in parts[0]:
                start_seconds = datetime.strptime(start_seconds_txt, '%M:%S')
                end_seconds = datetime.strptime(end_seconds_txt, '%M:%S')
            else:
                start_seconds = timedelta(seconds=int(start_seconds_txt))
                end_seconds = timedelta(seconds=int(end_seconds_txt))

            if topic not in primary_topic2duration:
                primary_topic2duration[topic] = datetime.strptime('00:0', '%M:%S')
            if topic not in secondary_topic2duration:
                secondary_topic2duration[topic] = datetime.strptime('00:0', '%M:%S')
            
            assert end_seconds >= start_seconds
            diff = end_seconds - start_seconds

            if topic_type == 'p':
                primary_topic2duration[topic] += diff
            else:
                secondary_topic2duration[topic]+= diff
    
    for key in sorted(secondary_topic2duration):
        output_str = str(key) + " " + str(secondary_topic2duration[key]).split(" ")[1]
        output_transcript_handle.write(output_str + '\n')


if __name__ == '__main__':
    main()