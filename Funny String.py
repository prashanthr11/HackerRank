#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    r = str()
    for i in range(len(s) - 1, -1, -1):
        r += s[i]
    r = list(map(str, r))
    l2 = list()
    l3 = list()
    d1 = list()
    d2 = list()
    for i in r:
        l2.append(ord(i))
    for i in s:
        l3.append(ord(i))
    for i in range(1, len(l2)):
        d1.append(abs(l2[i] - l2[i - 1]))
    for i in range(1, len(l3)):
        d2.append(abs(l3[i] - l3[i - 1]))
    if d1 == d2:
        return 'Funny'
    else:
        return 'Not Funny'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
