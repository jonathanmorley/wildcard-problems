#!/usr/bin/python3

import sys, getopt,itertools
from operator import itemgetter
from itertools import combinations

def main(argv):
    inputfile = ''
    helptext = 'test.py -i <inputfile>'
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print(helptext)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(helptext)
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    
    with open(inputfile) as f:
        generation, overhead, budget = [x.rstrip() for x in list(f)]
        generation = [int(x) for x in generation[1:-1].split(',')]
        overhead = [int(x) for x in overhead[1:-1].split(',')]
        cards = [x for x in zip(generation, overhead)]
        print(time(cards))
        combos = combinations(cards, 9)
        print(min([time(combo) for combo in combos]))
def time(cards):
    gentime = sum([x for x,_ in cards])
    overheadtime = sum([x for _,x in cards]) * (len(cards) - 1)
    return gentime + overheadtime

if __name__ == "__main__":
    main(sys.argv[1:])