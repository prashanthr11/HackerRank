#!/bin/python3

import math
import os
import random
import re
import sys

def beautifulTriplets(d, a):
    cnt = 0
    s = set(a)
    for i in range(len(a)):
        if a[i] + d in s and a[i] + d + d in s:
            cnt += 1
    return cnt


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
