'''Read and print an integer series.'''

import sys


def read_series(filename):
    try:
        f = open(filename, mode='rt', encoding='utf-8')
        return [int(line.strip()) for line in f]
        # series = []
        # for line in f:
        #     a = int(line.strip())
        #     series.append(a)
    finally:
        f.close()


def read_series_2(filename):  # using with block
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]


if __name__ == "__main__":
    read_series_2(filename=sys.argv[1])
