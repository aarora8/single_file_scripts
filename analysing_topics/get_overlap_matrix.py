#!/usr/bin/env python3
from datetime import datetime
from datetime import timedelta
from collections import namedtuple
from collections import defaultdict
import itertools
import numpy as np
# '<reco-id> <start-time> <end-time> <topic> <type>'

# global Segment 
segment = namedtuple('segment', 'reco_id start_time end_time topic_id topic_type')
topic_overlap = namedtuple('topic_overlap', 'reco_id topic_id1 topic_id2 duration')

def groupby(iterable, keyfunc):
    """Wrapper around ``itertools.groupby`` which sorts data first."""
    iterable = sorted(iterable, key=keyfunc)
    for key, group in itertools.groupby(iterable, keyfunc):
        yield key, group


def get_segments(text_file_data):
    segments = []
    # text file format: <reco-id> <start-time> <end-time> <topic> <type>
    for line in text_file_data:
        parts = line.strip().split()
        if len(parts) == 5:
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

            assert end_seconds >= start_seconds
            topic = parts[3] + '(' + parts[4] + ')'
            segments.append(segment(
                reco_id = parts[0],
                start_time = start_seconds,
                end_time = end_seconds,
                topic_id = topic,
                topic_type = parts[4]
            ))
            
    return segments


def get_topic_duration_vector(topic_segs):
    # 1 = 10 millisec
    # 12000 = 1200 sec = 20 mins
    vector_size = 12000
    topic_vector = np.zeros(vector_size, dtype = int)
    # reco_id start_time end_time topic_id topic_type
    for seg in topic_segs:
        start_time = seg.start_time
        start_time = int(start_time * 10)
        end_time = seg.end_time
        end_time = int(end_time * 10)
        topic_vector[start_time:end_time] = 1
    return topic_vector


def find_overlap_duration_between_two_topics(segs_topicid1, segs_topicid2):
    topicid1_vector = get_topic_duration_vector(segs_topicid1)
    topicid2_vector = get_topic_duration_vector(segs_topicid2)
    overlap_vector = topicid1_vector & topicid2_vector
    duration = np.sum(overlap_vector)
    return duration


def find_overlapping_segments(segs):
    reco_id = segs[0].reco_id
    topic2segs = defaultdict(list,
        {topic_id : list(g) for topic_id, g in groupby(segs, lambda x: x.topic_id)})

    tokens = []
    for topic_id1 in topic2segs.keys():
        for topic_id2 in topic2segs.keys():
            if topic_id1 == topic_id2:
                continue
            topicid1_segs = topic2segs[topic_id1]
            topicid2_segs = topic2segs[topic_id2]
            duration = find_overlap_duration_between_two_topics(topicid1_segs, topicid2_segs)
            if duration == 0:
                continue
            duration = duration/10
            tokens.append(topic_overlap(reco_id = reco_id, topic_id1 = topic_id1, topic_id2 = topic_id2, duration = duration))
    return tokens

def main():
    topic_text = '/Users/ashisharora/Desktop/root/corpora/TDCorpus/topic_text.txt'
    output_topic_info = '/Users/ashisharora/Desktop/root/toolkits/single_file_scripts/analysing_topics/output_files/recowise_topic_overlap_info.txt'
    output_topic_info = '/Users/ashisharora/Desktop/root/toolkits/single_file_scripts/analysing_topics/output_files/topic_overlap_info.txt'
    output_topic_handle = open(output_topic_info, 'w', encoding='utf8')

    # create segments from a text file of the following format
    # text file format: <reco-id> <start-time> <end-time> <topic> <type>
    text_file_handle = open(topic_text, 'r', encoding='utf8')
    text_file_data = text_file_handle.read().strip().split("\n")
    segments = get_segments(text_file_data)

    # We group the segment list into a dictionary indexed by reco_id
    reco2segs = defaultdict(list,
        {reco_id : list(g) for reco_id, g in groupby(segments, lambda x: x.reco_id)})

    overlap_list = []
    for reco_id in reco2segs.keys():
        segs = reco2segs[reco_id]
        overlap_list.extend(find_overlapping_segments(segs))

    # for _, topic_overlap in enumerate(overlap_list):
    #     output_topic_handle.write("Reco: {0} topic_id1: {1} topic_id2: {2} duration: {3}  (sec) \n".format(topic_overlap.reco_id, topic_overlap.topic_id1, topic_overlap.topic_id2, topic_overlap.duration))

    topic_overlap2duration= dict()
    for _, topic_overlap in enumerate(overlap_list):
        topics = topic_overlap.topic_id1 + '_' + topic_overlap.topic_id2
        if topics not in topic_overlap2duration:
            topic_overlap2duration[topics] = int(0)
        topic_overlap2duration[topics] += int(topic_overlap.duration)

    sorted_tokens =  dict(sorted(topic_overlap2duration.items(), key=lambda item: item[1], reverse=True))
    count = 0
    for topics in sorted_tokens:
        count += 1
        if count % 2 !=0:
            continue
        output_topic_handle.write("{0} {1} \n".format(topics, sorted_tokens[topics]))


if __name__ == '__main__':
    main()