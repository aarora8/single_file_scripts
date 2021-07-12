#!/usr/bin/python3
# This script visualize RTTM file with matplotlib
# "rttm: <type> <file-id> <channel-id> <begin-time> <duration> <NA> <NA> <speaker> <conf>"
# '<file-id> <start-time> <end-time> <speaker> <type>'

import matplotlib
matplotlib.use('Agg')
import numpy as np
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt

def main():
    rttm_filename = '/Users/ashisharora/Desktop/root/corpora/TDCorpus/topic_text.txt'
    uttname = '20200925_1525_0087_0088_01_01_toen.txt'
    uttname = '20200928_1150_0072_0071_04_01_toen.txt'

    '<file-id> <start-time> <end-time> <speaker> <type>'
    with open(rttm_filename, 'r') as fh:
        content = fh.readlines()

    start_time_list = []
    end_time_list = []
    speaker_list = []
    spkname_dict = {}
    num_spk = 0
    num_seg = 0
    for line in content:
        line = line.strip('\n')
        line_split = line.split()
        if line_split[0] != uttname:
            continue

        # uttname = line_split[0]
        num_seg += 1
        start_seconds_txt = line_split[1].strip().split('.')[0]
        end_seconds_txt = line_split[2].strip().split('.')[0]
        if ':' in line_split[1]:
            start_yms = datetime.strptime(start_seconds_txt, '%M:%S')
            start_seconds=(start_yms-datetime(1900,1,1)).total_seconds()
            end_yms = datetime.strptime(end_seconds_txt, '%M:%S')
            end_seconds=(end_yms-datetime(1900,1,1)).total_seconds()
        else:
            start_seconds = timedelta(seconds=int(start_seconds_txt))
            end_seconds = timedelta(seconds=int(end_seconds_txt))

        start_time = start_seconds
        end_time = end_seconds
        speaker = line_split[3]
        start_time_list.append(start_time)
        end_time_list.append(end_time)
        if speaker not in spkname_dict:
            num_spk += 1
            spkname_dict[speaker] = num_spk
        speaker_list.append(spkname_dict[speaker])

    # 00:06.503 00:11.384 hello p
    # 00:11.634 06:36.084 meeting-fu p
    # 01:16.376 01:45.281 transport s
    # 06:38.965 06:43.727 operator p

    from matplotlib import collections  as mc
    c = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]
    seg_list = []
    color_list = []
    for i in range(num_seg):
        # plt.plot(x, np.sin(x), '-g', label='sin(x)')
        # plt.plot(x, np.cos(x), ':b', label='cos(x)')
        print("speaker {}: {} start {} end".format(speaker_list[i], start_time_list[i], end_time_list[i]))
        seg_list.append([(start_time_list[i], speaker_list[i]), (end_time_list[i], speaker_list[i])])
        color_list.append(c[speaker_list[i] % 10])

    lc = mc.LineCollection(seg_list, colors=color_list, linewidths=2)

    plt.style.use('seaborn-whitegrid')
    fig = plt.figure()
    ax = plt.axes()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    # plt.xlim(-1, 410)
    # plt.ylim(1, 4)
    plt.title("A Sine Curve")
    # my_xticks = ['1', '2', '3', '4']
    # plt.yticks(x, my_xticks)
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    # plt.plot([], [], color="red", label="manual")
    # plt.legend(bbox_to_anchor=(1, 1), loc="upper left")
    # plt.show()
    fig.savefig("tmp.png")
    return 0

if __name__ == "__main__":
    main()