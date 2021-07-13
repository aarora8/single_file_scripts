#!/usr/bin/env python3
from datetime import datetime
from datetime import timedelta
from collections import namedtuple
from collections import defaultdict
import itertools
# '<reco-id> <start-time> <end-time> <topic> <type>'

# global Segment 
segment = namedtuple('segment', 'reco_id start_time end_time topic_id')

def groupby(iterable, keyfunc):
    """Wrapper around ``itertools.groupby`` which sorts data first."""
    iterable = sorted(iterable, key=keyfunc)
    for key, group in itertools.groupby(iterable, keyfunc):
        yield key, group


def get_segments(text_file_data, segment):
    segments = []
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
                topic_id = topic
            ))
            
    return segments


def find_single_speaker_segments(segs):
    # segment = namedtuple('segment', 'reco_id start_time end_time topic_id')
    # reco_id, start_time, dur, end_time, spk_id
    reco_id = segs[0].reco_id
    tokens = []
    for seg in segs:
        tokens.append(("BEG", seg.start_time, seg.topic_id))
        tokens.append(("END", seg.end_time, seg.topic_id))
    sorted_tokens = sorted(tokens, key=lambda x: x[1])

    single_speaker_segs = []
    running_spkrs = set()
    for token in sorted_tokens:
        if (token[0] == "BEG"):
            running_spkrs.add(token[2])
            if (len(running_spkrs) == 1):
                seg_begin = token[1]
                cur_spkr = token[2]
            elif (len(running_spkrs) == 2):
                single_speaker_segs.append(segment(reco_id, seg_begin, end_time=token[1], topic_id=cur_spkr))
        elif (token[0] == "END"):
            try:
                running_spkrs.remove(token[2])
            except:
                Warning ("Speaker not found")
            if (len(running_spkrs) == 1):
                seg_begin = token[1]
                cur_spkr = list(running_spkrs)[0]
            elif (len(running_spkrs) == 0):
                single_speaker_segs.append(segment(reco_id, seg_begin, token[1], topic_id=cur_spkr))
    
    return single_speaker_segs


def find_overlapping_segments(segs, label):
    reco_id = segs[0].reco_id
    tokens = []
    for seg in segs:
        tokens.append(("BEG", seg.start_time, seg.topic_id))
        tokens.append(("END", seg.end_time, seg.topic_id))
    sorted_tokens = sorted(tokens, key=lambda x: x[1])

    running_spkrs = set()
    overlap_segs = []
    spkr_count = 0
    ovl_begin = 0
    ovl_end = 0
    for token in sorted_tokens:
        if (token[0] == "BEG"):
            spkr_count +=1
            running_spkrs.add(token[2])
            if (spkr_count == 2):
                ovl_begin = token[1]
        else:
            spkr_count -= 1
            if (spkr_count == 1):
                ovl_end = token[1]
                label = str(running_spkrs)
                running_spkrs = set()
                overlap_segs.append(segment(reco_id, ovl_begin, ovl_end, topic_id=label))
    
    return overlap_segs


def main():
    topic_text = '/Users/ashisharora/Desktop/root/corpora/TDCorpus/topic_text.txt'
    output_topic_info = '/Users/ashisharora/Desktop/root/toolkits/single_file_scripts/analysing_topics/overlap_info.txt'
    output_topic_handle = open(output_topic_info, 'w', encoding='utf8')

    # create segments from a text file of the following format
    # text file format: <reco-id> <start-time> <end-time> <topic> <type>
    text_file_handle = open(topic_text, 'r', encoding='utf8')
    text_file_data = text_file_handle.read().strip().split("\n")
    segments = get_segments(text_file_data, segment)

    # We group the segment list into a dictionary indexed by reco_id
    reco2segs = defaultdict(list,
        {reco_id : list(g) for reco_id, g in groupby(segments, lambda x: x.reco_id)})


    overlap_segs = []
    for reco_id in reco2segs.keys():
        segs = reco2segs[reco_id]
        overlap_segs.extend(find_overlapping_segments(segs, 'overlap'))


    for _, seg in enumerate(overlap_segs):
        # print(seg)
        output_topic_handle.write("Reco: {0} Start time: {1} End time: {2} Topics: {3} \n".format(seg.reco_id, seg.start_time, seg.end_time, seg.topic_id))


if __name__ == '__main__':
    main()