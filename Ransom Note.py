#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(m, n):
    for i in n:
        if i in m:
            flag = True
            m.remove(i)
            n.remove(i)
        else:
            flag = False
            break
    if flag:
        print('Yes')
    else:
        print('No')
            


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
