import fileinput
import argparse
from sys import stdin

parser = argparse.ArgumentParser(description="my cat command")

parser.add_argument('files', nargs='*')
parser.add_argument('-n', action='store_true')

args = parser.parse_args()


def print_line(line, number=0):
    if args.n:
        spaces = 6 - len(str(number))
        space = ' '
        print(f'{space*spaces}{number}  {line}', end='')
    else:
        print(line, end='')


if args.files:
    for filename in args.files:
        with open(filename, 'r') as f:
            linenumber = 1
            for line in f.readlines():
                print_line(line, linenumber)
                linenumber += 1
else:
    linenumber = 1
    # for line in fileinput.input():
    #     print_line(line, linenumber)
    #     linenumber += 1
    while True:
        my_input = input()
        print_line(my_input)
