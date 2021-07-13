#!/usr/bin/env python3
from datetime import datetime
from datetime import timedelta
def main():
    topic_text = '/Users/ashisharora/Desktop/root/corpora/TDCorpus/topic_text.txt'
    output_ptopic_info = '/Users/ashisharora/Desktop/root/toolkits/single_file_scripts/analysing_topics/primary_duration.txt'
    output_ptopic_handle = open(output_ptopic_info, 'w', encoding='utf8')
    output_stopic_info = '/Users/ashisharora/Desktop/root/toolkits/single_file_scripts/analysing_topics/secondary_duration.txt'
    output_stopic_handle = open(output_stopic_info, 'w', encoding='utf8')
    
    text_file_handle = open(topic_text, 'r', encoding='utf8')
    text_file_data = text_file_handle.read().strip().split("\n")    
    primary_topic2duration = dict()
    secondary_topic2duration = dict()
    for line in text_file_data:
        parts = line.strip().split()
        if len(parts) == 5:
            topic_type = parts[4].strip().split()[0]
            topic = parts[3] + '(' + parts[4] + ')'
            start_seconds_txt = parts[1].strip().split('.')[0]
            end_seconds_txt = parts[2].strip().split('.')[0]
            if ':' in parts[1]:
                start_seconds = datetime.strptime(start_seconds_txt, '%M:%S')
                end_seconds = datetime.strptime(end_seconds_txt, '%M:%S')
            else:
                start_seconds = timedelta(seconds=int(start_seconds_txt))
                end_seconds = timedelta(seconds=int(end_seconds_txt))

            assert end_seconds >= start_seconds
            diff = end_seconds - start_seconds
            diff = diff.total_seconds()
            if 'p' in topic_type:
                if topic not in primary_topic2duration:
                    primary_topic2duration[topic] = list()
                primary_topic2duration[topic].append(diff)
            else:
                if topic not in secondary_topic2duration:
                    secondary_topic2duration[topic] = list()
                secondary_topic2duration[topic].append(diff)
    
    for key in sorted(primary_topic2duration):
        output_str = str(key)
        for _, val in enumerate(primary_topic2duration[key]):
            output_str = output_str + " " + str(val)
        output_ptopic_handle.write(output_str + '\n')

    for key in sorted(secondary_topic2duration):
        output_str = str(key)
        for _, val in enumerate(secondary_topic2duration[key]):
            output_str = output_str + " " + str(val)
        output_stopic_handle.write(output_str + '\n')


if __name__ == '__main__':
    main()