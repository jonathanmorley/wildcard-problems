#!/usr/bin/python3

import sys, getopt
from itertools import permutations

def main(argv):
    inputfile = ''
    helptext = 'problem1.py -i <inputfile>'
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
        rows = [row.rstrip() for row in list(f)]
        columns = [''.join(list(column)) for column in zip(*rows)]
        validlines = [line.count('*') for line in rows+columns if line.count('*') >= 5]
        perms = [sum(1 for _ in permutations(range(spaces), 5)) for spaces in validlines]
        print(sum(perms))

if __name__ == "__main__":
    main(sys.argv[1:])