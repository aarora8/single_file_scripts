#!/usr/bin/env python3

from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
global num_exp


def open_setments(segments):
    # segments:  <utterance-id> <recording-id> <segment-begin> <segment-end>
    # topics: <file-id> <start-time> <end-time> <speaker> <type>
    # super_id = file-id
    # this script is creating an stm file using kaldi segments and text file
    seg_dict = defaultdict(list)
    with open(segments, 'r') as seg:
        for line in seg.readlines():
           utt_id, super_id, start_time, end_time = line.strip().split()
           seg_dict[super_id].append((float(start_time), float(end_time), utt_id))

    for super_id in seg_dict.keys():
        seg_dict[super_id].sort(key=lambda x: (x[0], x[1]))
    return seg_dict


def print_setments(seg_dict):
    for super_id in seg_dict.keys():
        print(super_id)
        for u in seg_dict[super_id]:
            print("\t%s" % str(u))


def plot_a_recording(super_id, utts, x1, y1, width, color, has_text=False):
    # (x1, y1) is the bottom-left corner of the canvas

    if has_text:
        t = super_id[: super_id.rfind("_")]
        plt.text(x1, y1 + num_exp, "%s:" % t, fontsize=4)

    for u in utts:
        x, y = [x1 + (u[0] / 180) * width, x1 + (u[1] / 180) * width], [y1, y1]
        # print(str(x), str(y))
        # plt.plot(x, y, marker='o', color=color)
        plt.plot(x, y, color=color)

        x, y = [x1 + (u[1] / 180) * width - 0.01, x1 + (u[1] / 180) * width], [y1, y1]
        plt.plot(x, y, color='black')


def plot_recordings(seg_dict, x0, y0, color, has_text=False):
    x1 = x0
    y1 = y0
    cnt = 0
    width = 60
    for super_id in seg_dict.keys():
        print(cnt, super_id)
        if cnt % 25 == 0:
            x1 = x0 + int(cnt / 25) * (width + 10)
            y1 = y0

        plot_a_recording(super_id, seg_dict[super_id], x1, y1, width, color, has_text=has_text)

        y1 += 3.5 + num_exp
        cnt += 1


# https://canvasjs.com/javascript-charts/line-chart-zoom-pan/
if __name__ == '__main__':
    segments1 = '/Users/ashisharora/Desktop/root/corpora/TDCorpus/topic_text.txt'
    seg_dict1 = open_setments(segments1)
    print_setments(seg_dict1)

    # layout design:
    # 4 columns, 25 recordings for each column
    # x width: (60 + 10) * 4 - 10 = 270
    # y width: 4 * 25 = 100

    # example of drawing lines
    # x1, y1 = [-1, 1000], [4, 4]
    # x2, y2 = [1, 3], [2, 2]
    # plt.plot(x1, y1, marker='o', color='red')
    # plt.plot(x2, y2, marker='o', color='blue')
    # plt.show()

    num_exp = 6
    plt.figure(figsize=(20, 7+((num_exp + 1)/2)))
    plot_recordings(seg_dict1, 0, 1, "red", has_text=True)
    plt.plot([], [], color="red", label="manual")
    plt.legend(bbox_to_anchor=(1, 1), loc="upper left")
    plt.show()