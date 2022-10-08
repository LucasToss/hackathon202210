#! /usr/bin/python3

# Check if all input files are processed
# Called in pipe:
#  ssh ... "ls -d /data/output/*" | ./wait_end.py

import sys, os

def main():
    input_files =  os.listdir('input')
    output_files = os.listdir('output')
    # output_files = sorted([line.split('/')[-1].split('.')[0] for line in sys.stdin])

    finished = input_files==output_files
    print(f"input_files: {input_files} output_files: {output_files} finished: {finished}")

    return 0 if finished else 1


if __name__ == '__main__':
    sys.exit(main())