#!/bin/python3

import math
import os
import random
import re
import sys
import string

def pangrams(s):
    s = s.lower()
    s = set(s)
    L_C = set(string.ascii_lowercase)
    if L_C.issubset(s):
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
