#!/bin/python3

import math
import os
import random
import re
import sys


def taumBday(b, w, bc, wc, z):
    if bc == wc:
        return min((bc * b) + (wc * w), wc * (b + w))
    return min((bc * b) + (wc * w), bc * (b + w) + (w * z), wc * (b + w) + (b * z))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
