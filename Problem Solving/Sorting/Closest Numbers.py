#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(a):
    mini = 1e11
    a.sort()
    for i in range(1, len(a)):
        if abs(a[i] - a[i - 1] < mini):
            x, y = a[i - 1], a[i]
            mini = abs(a[i - 1] - a[i])
    return x, y


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
