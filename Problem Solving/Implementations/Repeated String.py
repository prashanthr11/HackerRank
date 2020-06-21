#!/bin/python3

import math
import os
import random
import re
import sys

def repeatedString(s, n):
    if len(s) < n:
        cnt = s.count('a') * (n // len (s))
        return cnt + repeatedString(s, n % len(s))

    else:
        s = s[:n]
        return s.count('a')
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
