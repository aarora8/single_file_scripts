#!/usr/bin/env python
import re
UNK = '<UNK>'

def case_normalize(w):
    if w.startswith('~'):
        return w.upper()
    else:
        return w.lower()


def process_transcript(transcript):
    global WORDLIST
    # https://www.programiz.com/python-programming/regex
    # [] for set of characters you with to match
    # eg. [abc] --> will search for a or b or c
    # "." matches any single character
    # "$" to check if string ends with a certain character 
    # eg. "a$" should end with "a"
    # replace <extreme background> with <extreme_background>
    # replace <foreign lang="Spanish">fuego</foreign> with foreign_lang=
    # remove "[.,!?]"
    # remove " -- "
    # remove " --" --> strings that ends with "-" and starts with " "
    # \s+ markers are – that means “any white space character, one or more times”
    tmp = re.sub(r'<extreme background>', '<extreme_background>', transcript)
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
    sups = "Hello my name is ashish"
    print(sups)
    cleaned_transcrition = process_transcript(sups)
    print(cleaned_transcrition)

if __name__ == '__main__':
    main()