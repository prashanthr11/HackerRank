#!/bin/python3

import math
import os
import random
import re
import sys


def icecreamParlor(m, a):
    i = 0
    while True:
        d = m - a[i]
        a[i] = -1e7
        if d in a:
            return sorted([i + 1, a.index(d) + 1])
        i += 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
