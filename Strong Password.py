#!/bin/python3

import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    d = dict()
    d['Nflag'] = d['Lflag'] = d['Uflag'] = d['Sp_flag'] = False
    for i in password:
        if i in numbers:
            d['Nflag'] = True
        if i in lower_case:
            d['Lflag'] = True
        if i in upper_case:
            d['Uflag'] = True
        if i in special_characters:
            d['Sp_flag'] = True
    
    val = list(d.values())
    if n < 6:
        return max(abs(n - 6), val.count(False))
    return val.count(False)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
