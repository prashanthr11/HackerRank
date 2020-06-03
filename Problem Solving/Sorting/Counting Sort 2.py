#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the countingSort function below.
def countingSort(a):
    d = Counter(a)
    l = list()
    for k in d:
        while d[k] > 0:
            l.append(k)
            d[k] -= 1
    return sorted(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
