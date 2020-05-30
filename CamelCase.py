#!/bin/python3

import math
import os
import random
import re
import sys
import string

def camelcase(s):
    cnt = 1
    U_C = string.ascii_uppercase
    for i in s:
        if i in U_C:
            cnt += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
