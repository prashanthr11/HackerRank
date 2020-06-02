#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the missingNumbers function below.
def missingNumbers(a, b):
    d1 = Counter(a)
    d2 = Counter(b)
    s = set()
    for k in d1:
        if d1[k] == d2[k]:
            pass
        else:
            s.add(k)
    for k in d2:
        if d1[k] == d2[k]:
            pass
        else:
            s.add(k)
    l = list(s)    
    l.sort()
    return l 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
