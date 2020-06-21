#!/bin/python3

import os
import sys
from math import floor, ceil


def halloweenParty(k):
    return int(floor(k / 2) * ceil(k / 2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        k = int(input())

        result = halloweenParty(k)

        fptr.write(str(result) + '\n')

    fptr.close()
