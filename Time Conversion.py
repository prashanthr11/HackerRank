#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    h, m, se = list(map(str, s.split(':')))
    if se[-2] == 'P':
        h = int(h)
        h = (h % 12) + 12
    elif h == str(12):
        h = "00"
    st = "{}:{}:{}".format(h, m, se[:2])
    return st

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
