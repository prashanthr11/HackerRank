#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    hours = ["twelve", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven"]
    minutes = hours
    minutes[0] = "o' clock"
    temp = ["twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]
    minutes += temp
    if m == 0:
        return "{} {}".format(hours[h % 12], minutes[m])
    if m == 30 or m == 15:
        return "{} past {}".format(minutes[m], hours[h % 12])
    if m == 45:
        return "{} to {}".format(minutes[60 - m], hours[(h % 12) + 1])
    if m == 1:
        return "{} minute past {}".format(minutes[m], hours[h % 12])
    if m == 59:
        return "{} minute to {}".format(minutes[m], hours[(h % 12) + 1])
    if m < 30:
        return "{} minutes past {}".format(minutes[m], hours[h % 12])
    else:
        return "{} minutes to {}".format(minutes[60 - m], hours[(h % 12) + 1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
