#!/bin/python3

import math
import os
import random
import re
import sys

def rev(i):
    s = str(i)
    s = s[::-1]
    return int(s)

def beautifulDays(i, j, k):
    cnt = 0
    for i in range(i, j + 1):
        if abs(i - rev(i)) % k == 0:
            cnt += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
