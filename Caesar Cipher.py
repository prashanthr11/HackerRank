import string

U_C = string.ascii_uppercase
upper = list(U_C)

L_C = string.ascii_lowercase
lower = list(L_C)

n = int(input())
s = list(map(str, input()))
k = int(input())

for i in range(len(s)):
    if s[i] in U_C:
        s[i] = upper[(U_C.find(s[i]) + k) % 26]
    elif s[i] in L_C:
        s[i] = lower[(L_C.find(s[i]) + k) % 26]
    else:
        pass

for i in s:
    print(i, end = '')