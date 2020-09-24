#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def prefix(l):
    x = []
    if len(l):
        x.append(l[0])
        for i in range(1, len(l)):
            x.append(x[i - 1] + l[i])

    return set(x)

def equalStacks(h1, h2, h3):
    h1.reverse()
    h2.reverse()
    h3.reverse()
    a, b, c = prefix(h1), prefix(h2), prefix(h3)
    maxi = 0
    tmp = a.intersection(b.intersection(c))
    if len(tmp):
        return max(tmp)
    return maxi

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
