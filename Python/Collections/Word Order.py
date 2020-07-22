from collections import OrderedDict

d = OrderedDict()
for i in range(int(input())):
    s = input()
    d[s] = d.get(s, 0) + 1

print(len(d))
for i in d:
    print(d[i], end = " ")

