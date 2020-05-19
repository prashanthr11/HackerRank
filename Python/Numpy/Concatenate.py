import numpy as np

s = input().split()
l = []

for i in range(int(s[0]) + int(s[1])):
    d = input().split()
    l.append((int(d[0]), int(d[1])))

print(np.array(l))
