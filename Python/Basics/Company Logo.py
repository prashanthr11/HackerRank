#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter



if __name__ == '__main__':
    s = input()
    d = Counter(s)
    cnt = 0
    for k, v in sorted(d.items(), key=lambda x:x[1], reverse=True):
        print(k, v)
        cnt += 1
        if cnt == 3:
            break