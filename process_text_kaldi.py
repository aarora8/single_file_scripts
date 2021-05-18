#!/usr/bin/env python3
# coding: utf-8
import sys
import re

WORDLIST = dict()
IV_WORDS = dict()
OOV_WORDS = dict()
UNK = '<UNK>'
REPLACE_UNKS = True


def case_normalize(w):
    if w.startswith('~'):
        return w.upper()
    else:
        return w.lower()


def process_line(line):
    global WORDLIST
    tmp = re.sub(r'extreme\s+background', 'extreme_background', line)
    tmp = re.sub(r'foreign\s+lang=', 'foreign_lang=', tmp)
    tmp = re.sub(r'\)\)([^\s])', ')) \1', tmp)
    tmp = re.sub(r'[.,!?]', ' ', tmp)
    tmp = re.sub(r' -- ', ' ', tmp)
    tmp = re.sub(r' --$', '', tmp)
    x = re.split(r'\s+', tmp)
    old_x = x
    x = list()

    w = old_x.pop(0)
    while old_x:
        if w.startswith(r'(('):
            while old_x and not w.endswith('))'):
                w2 = old_x.pop(0)
                w += ' ' + w2
                #print(w, file=sys.stderr)
            x.append(w)
            if old_x:
                w = old_x.pop(0)
        elif w.startswith(r'<'):
            #this is very simplified and assumes we will not get a starting tag
            #alone
            while old_x and not w.endswith('>'):
                w2 = old_x.pop(0)
                w += ' ' + w2
            x.append(w)
            if old_x:
                w = old_x.pop(0)
        elif w.endswith(r'))'):
            print('error ' + w, file=sys.stderr)
            if old_x:
                w = old_x.pop(0)
        else:
            x.append(w)
            if old_x:
                w = old_x.pop(0)

    if not x:
        return None
    if len(x) == 1 and x[0] in ('<background>', '<extreme_background>'):
        return None

    out_x = list()
    for w in x:
        w = case_normalize(w)
        out_x.append(w)

    return ' '.join(out_x)

def main():
    sups = " a big explosion and "
    print(sups)
    cleaned_transcrition = process_line(sups)
    print(cleaned_transcrition)

if __name__ == '__main__':
    main()