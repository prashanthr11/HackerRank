#!/bin/python3

import math
import os
import random
import re
import sys

def marsExploration(s):
    s1 = "SOS" * int(len(s) / 3)
    cnt = 0
    for i in range(len(s)):
        if s[i] != s1[i]:
            cnt += 1
            
    return cnt

    if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
