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
        rows = [row.rstrip() for row in list(f)]
        columns = [''.join(list(column)) for column in zip(*rows)]
        validlines = [line.count('*') for line in rows+columns if line.count('*') >= 5]
        perms = [sum(1 for _ in permutations(range(spaces), 5)) for spaces in validlines]
        print(perms)
        print(sum(perms))
        #print(*validlines, sep='\n')
        #print(len(validlines))

if __name__ == "__main__":
    main(sys.argv[1:])