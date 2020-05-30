#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    d = Counter(s)
    l = list(d.values())
    cnt = 0
    for i in l:
        if i % 2:
            cnt += (i % 2)
    if cnt < 2:
        return "YES"
    else:
        return "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
