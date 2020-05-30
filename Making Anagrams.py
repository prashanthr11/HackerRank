#!/bin/python3

import math
import os
import random
import re
import sys
# from collections import Counter

def makingAnagrams(s1, s2):
    d = dict()
    for i in s1:
        d[i] = d.get(i, 0) + 1
    for i in s2:
        d[i] = d.get(i, 0) - 1
    l = list(d.values())
    for i in range(len(l)):
        if l[i] < 0:
            l[i] = abs(l[i])

    return sum(l)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
