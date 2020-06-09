#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(a):
    ls = list()
    while True:
        if len(a) != 0:
            mini = min(a)
            for i in range(len(a)):
                a[i] -= mini
            ls.append(len(a))
            a = [i for i in a if i != 0]
        else:
            return ls


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
