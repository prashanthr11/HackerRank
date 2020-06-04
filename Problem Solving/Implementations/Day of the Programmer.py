from calendar import isleap
from sys import exit

def Gregorian_isleap(n):
    return isleap(n)

def Julian_isleap(n):
    return n % 4 == 0


n = int(input())
flag = True
if n == 1918:
    print("26.09.1918")
    exit()
if n >= 1700 and n <= 1917:
    flag = Julian_isleap(n)
else:
    flag = Gregorian_isleap(n)


if flag:
    print("12.09." + str(n))
else:
    print("13.09." + str(n))
