#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
def equalizeArray(a):
    d = Counter(a)
    heightest = d.most_common(1)
    l = list(d.values())
    return sum(l) - heightest[0][1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
