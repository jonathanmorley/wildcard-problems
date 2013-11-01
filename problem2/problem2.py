#!/usr/bin/python3

import sys, getopt,itertools
from operator import itemgetter

def main(argv):
    inputfile = ''
    helptext = 'problem2.py -i <inputfile>'
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
        budget = int(budget)
        cards = [x for x in zip(generation, overhead)]
        cards = sorted(cards, key=itemgetter(0))
        cards = sorted(cards, key=itemgetter(1))
        for x in range(len(cards)):
            if time(cards[0:x]) > budget:
                print(x-1)
                break
        
def time(cards):
    gentime = sum([x for x,_ in cards])
    overheadtime = sum([x for _,x in cards]) * (len(cards) - 1)
    return gentime + overheadtime

if __name__ == "__main__":
    main(sys.argv[1:])