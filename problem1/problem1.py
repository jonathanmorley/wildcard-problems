#!/usr/bin/python3

import sys, getopt,itertools

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
        rows = [line.rstrip() for line in list(f)]
        count = len([row for row in rows if row.count('*') >= 5])
        columns = [''.join(list(i)) for i in itertools.zip_longest(*rows, fillvalue='X')]
        count += len([column for column in columns if column.count('*') >= 5])
        print(count)

if __name__ == "__main__":
    main(sys.argv[1:])