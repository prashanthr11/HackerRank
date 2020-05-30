#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    l = list(map(str, s))
    d = dict()
    pos = neg = 0
    
    for i in range(len(l)//2):
        d[l[i]] = d.get(l[i], 0) + 1
    
    for i in range(len(l)//2, len(l)):
        d[l[i]] = d.get(l[i], 0) - 1
    
    l2 = list(d.values())
    
    for i in l2:
        if i > 0:
            pos += i
        elif i < 0:
            neg += i
            
    return max(pos, neg)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
