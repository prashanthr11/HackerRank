#!/bin/python3

import math
import os
import random
import re
import sys

def hackerrankInString(s):
    # s1 = ['h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k']
    s1 = list(map(str, "hackerrank"))
    flag = False
    for i in s:
        if len(s1):
            if i == s1[0]:
                del s1[0]
    if len(s1):
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
