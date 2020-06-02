#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the counterGame function below.
def counterGame(n):
    i = 0
    winner = 1
    while True:
        if pow(2, i) > n:
            n -= pow(2, i - 1)
            winner = not winner
            if n == 1:
                break
            else:
                i = 0
            # break
        if pow(2, i) == n:
            n /= 2
            winner = not winner
            if n == 1:
                break
            else:
                i = 0
        else:
            i += 1
    if winner:
        return 'Richard'
    else:
        return 'Louise '
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
