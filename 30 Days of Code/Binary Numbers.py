#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    cnt = 0
    l = list(map(int, bin(n)[2:]))
    t = 0
    for i in range(len(l)):
        if l[i] == 1:
            cnt += 1
        else:
            t = max(t, cnt)
            cnt = 0
    t = max(t, cnt)
print(t)
