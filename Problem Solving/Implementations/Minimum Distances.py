#!/bin/python3

import math
import os
import random
import re
import sys


def minimumDistances(a):
    if len(a) == len(set(a)):
        return -1
    mini = 1e5
    cnt = 1e5
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                cnt = abs(j - i)
            mini = min(mini, cnt)
    return mini

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
