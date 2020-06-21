#!/bin/python3

import math
import os
import random
import re
import sys


def jumpingOnClouds(c):
    i = 0
    cnt = 0
    while (i + 2) < len(c):
        cnt += 1
        if c[i + 2]:
            i += 1
        else:
            i += 2
    if i != len(c) - 1:
        cnt += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
