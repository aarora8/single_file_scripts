#!/usr/bin/python3
# This script visualize Topics
# The input file format should be as follows:
# '<reco-id> <start-time> <end-time> <topic> <type>'

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from collections import namedtuple


def main():
    
    topic_text = '/Users/ashisharora/Desktop/root/corpora/TDCorpus/topic_text.txt'
    output_topic_info = '/Users/ashisharora/Desktop/root/toolkits/single_file_scripts/analysing_topics/visualization.txt'
    output_topic_handle = open(output_topic_info, 'w', encoding='utf8')
    text_file_handle = open(topic_text, 'r', encoding='utf8')
    text_file_data = text_file_handle.read().strip().split("\n")    
    Segment = namedtuple('Segment', 'reco topic topicid start end type')
    curr_reco = text_file_data[0].strip().split()[0]
    prev_reco = text_file_data[0].strip().split()[0]
    segments = list()
    topic_dict = dict()
    topic_dict2 = dict()
    for line in text_file_data:
        parts = line.strip().split()
        if len(parts) == 5:
            curr_reco = parts[0]
            if prev_reco != curr_reco:
                # print('new recording')
                output_topic_handle.write('new recording' + '\n')
                # plot the segments
                plt.style.use('seaborn-whitegrid')
                fig = plt.figure()
                ax = plt.axes()
                # plotting horizontal lines with labels and colors
                c = ['blue', 'orange', 'green', 'red', 'purple', 'black', 'yellow', 'pink', 'cyan', 'magenta']
                for _, seg in enumerate(segments):
                    # print(' Reco: {} Topic: {}  Start time: {}  End time: {} '.format(prev_reco, seg.topic, seg.start, seg.end))
                    output_topic_handle.write("Reco: {0} Topic: {1} Start time: {2} End time: {3} \n".format(prev_reco, seg.topic, seg.start, seg.end))
                    # add label only if it is a new label
                    str_label = seg.topic
                    if str_label not in topic_dict2:
                        topic_dict2[str_label] = len(topic_dict2)
                        ax.hlines(y=seg.topicid, xmin=seg.start, xmax=seg.end, label=str_label, linewidth=2, color=c[seg.topicid% 10])
                    ax.hlines(y=seg.topicid, xmin=seg.start, xmax=seg.end, linewidth=2, color=c[seg.topicid% 10])
                
                ax.autoscale()
                ax.margins(0.1)

                # Shrink current axis by 20%
                box = ax.get_position()
                ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
                # adding title, names to x-axis, y-axis, legends, image name
                plt.title(str(prev_reco))
                plt.xlabel('Seconds')
                plt.ylabel('Topic ID')
                plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
                image_path= 'images/' + str(prev_reco) + '.png'
                fig.savefig(image_path)

                # update the book keeping variables
                prev_reco = curr_reco
                segments = []
                topic_dict = {}
                topic_dict2 = {}

            # get start and end time in seconds
            start_seconds_txt = parts[1].strip().split('.')[0]
            end_seconds_txt = parts[2].strip().split('.')[0]
            if ':' in parts[1]:
                start_yms = datetime.strptime(start_seconds_txt, '%M:%S')
                start_seconds=(start_yms-datetime(1900,1,1)).total_seconds()
                end_yms = datetime.strptime(end_seconds_txt, '%M:%S')
                end_seconds=(end_yms-datetime(1900,1,1)).total_seconds()
            else:
                start_seconds = timedelta(seconds=int(start_seconds_txt)).total_seconds()
                end_seconds = timedelta(seconds=int(end_seconds_txt)).total_seconds()

            # get topic and topic id
            topic = parts[3] + '(' + parts[4] + ')'
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
    return 0

if __name__ == "__main__":
    main()