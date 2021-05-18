#!/usr/bin/env python


def get_recording_details():
    # AMI_ES2011a_H00 1113.845
    # <reco-id> <dur>
    # AMI_ES2011a_H00_FEE041_0003427_0003714 AMI_ES2011a_H00 34.27 37.14
    # <utt-id> <reco-id> <seg-beg> <seg-end>
    recoid_dur_dict= {}
    for line in open('/Users/ashisharora/Desktop/corpora/kaldi_data_icsi/train_cleaned_fixed/reco2dur'):
        parts = line.strip().split()
        recoid_dur_dict[parts[0]]=parts[1]
    return recoid_dur_dict


def get_utterance_details():
    # AMI_ES2011a_H00_FEE041_0003427_0003714 AMI_ES2011a_H00 34.27 37.14
    # <utt-id> <reco-id> <seg-beg> <seg-end>
    uttid_dur_dict= {}
    for line in open('/Users/ashisharora/Desktop/corpora/kaldi_data_icsi/train_cleaned_fixed/segments'):
        parts = line.strip().split()
        uttid_dur_dict[parts[0]]=(parts[1],parts[3])
    return uttid_dur_dict


def main():
    reco_dict = get_recording_details()
    utt_dict = get_utterance_details()
    for key in utt_dict:
        recoid = utt_dict[key][0]
        recodur = reco_dict[recoid]
        utt_end = utt_dict[key][1]
        if float(utt_end) > float(recodur):
            print(key, utt_dict[key])
            print(recoid, reco_dict[recoid])


if __name__ == '__main__':
    main()