#!/usr/bin/python3
# This script visualize RTTM file with matplotlib
# "rttm: <type> <reco-id> <channel-id> <begin-time> <duration> <NA> <NA> <speaker> <conf>"
# '<reco-id> <start-time> <end-time> <speaker> <type>'

import matplotlib
matplotlib.use('Agg')
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
from collections import namedtuple

def main():
    '<reco-id> <start-time> <end-time> <topic> <type>'
    topic_text = '/Users/ashisharora/Desktop/root/corpora/TDCorpus/topic_text.txt'
    text_file_handle = open(topic_text, 'r', encoding='utf8')
    text_file_data = text_file_handle.read().strip().split("\n")
    
    uttname = '20200925_1525_0087_0088_01_01_toen.txt'
    uttname = '20200928_1150_0072_0071_04_01_toen.txt'
    topic_dict = {}
    Segment = namedtuple('Segment', 'reco topic topicid start end type')
    segments = []
    for line in text_file_data:
        line = line.strip('\n')
        parts = line.split()
        if parts[0] != uttname:
            continue

        # get start and end time in seconds
        start_seconds_txt = parts[1].strip().split('.')[0]
        end_seconds_txt = parts[2].strip().split('.')[0]
        if ':' in parts[1]:
            start_yms = datetime.strptime(start_seconds_txt, '%M:%S')
            start_seconds=(start_yms-datetime(1900,1,1)).total_seconds()
            end_yms = datetime.strptime(end_seconds_txt, '%M:%S')
            end_seconds=(end_yms-datetime(1900,1,1)).total_seconds()
        else:
            start_seconds = timedelta(seconds=int(start_seconds_txt))
            end_seconds = timedelta(seconds=int(end_seconds_txt))

        # get topic and topic id
        topic = parts[3]
        if topic not in topic_dict:
            topic_dict[topic] = len(topic_dict)

        # create segment
        segments.append(Segment(
                reco = parts[0],
                topic = topic,
                topicid = topic_dict[topic],
                start = start_seconds,
                end = end_seconds,
                type = parts[4]
            ))
    
    # plot the segments
    plt.style.use('seaborn-whitegrid')
    fig = plt.figure()
    ax = plt.axes()

    c = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'yellow', 'cyan', 'magenta']
    for _, seg in enumerate(segments):
        # print("Topic {}: {} start {} end".format(seg.topicid, seg.start, seg.end))
        ax.hlines(y=seg.topicid, xmin=seg.start, xmax=seg.end, label=seg.topic, linewidth=2, color=c[seg.topicid% 10])
    
    ax.autoscale()
    ax.margins(0.1)
    # Shrink current axis by 20%
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    plt.title(str(uttname))
    plt.xlabel('Seconds')
    plt.ylabel('Topic ID')
    # plt.legend(loc='upper left')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    image_name = str(uttname)+'.png'
    fig.savefig(image_name)
    return 0

if __name__ == "__main__":
    main()