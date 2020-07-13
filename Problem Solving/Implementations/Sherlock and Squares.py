#!/bin/python3

import math
import os
import random
import re
import sys


def squares(a, b):
    ans = list()
    for i in range(b + 1):
        x = pow(i, 2)
        if x <= b:
            ans.append(x)
        else:
            break
        
    ans = [i for i in ans if i >= a and i <= b]
    return len(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
