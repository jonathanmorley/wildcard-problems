#!/usr/bin/python3

import sys, getopt,itertools
from itertools import permutations,chain,repeat,islice

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
        generation, overhead, budget = list(f)
        print(generation)

if __name__ == "__main__":
    main(sys.argv[1:])