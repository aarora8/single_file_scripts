#!/usr/bin/env python3

import glob
def main():
    list_of_files = glob.glob('/Users/ashisharora/Desktop/root/corpora/TDCorpus/topics/*.txt')
    output_transcript = '/Users/ashisharora/Desktop/root/corpora/TDCorpus/conversation_topic_count_pr_sec'
    output_transcript_handle = open(output_transcript, 'w', encoding='utf8')
    for file_name in list_of_files:
        count_primary_topics = 0
        count_secondary_topics = 0
        text_file_handle = open(file_name, 'r', encoding='utf8')
        text_file_data = text_file_handle.read().strip().split("\n")
        file_name = file_name.strip().split('/')[-1]
        for line in text_file_data:
            parts = line.strip().split()
            if len(parts) == 4:
                topic_type = parts[3].strip().split()[0]
                if topic_type == 'p':
                    count_primary_topics += 1
                else:
                    count_secondary_topics +=1
            else:
                print(len(parts))
                print(line)
        output_transcript_handle.write(file_name + " " + str(count_primary_topics) + " " 
        + str(count_secondary_topics) + '\n')


if __name__ == '__main__':
    main()