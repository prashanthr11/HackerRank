from collections import OrderedDict
d = OrderedDict()
for i in range(int(input())):
    s = input().split()
    if len(s) == 2:
        d[s[0]] = d.get(s[0], 0) + int(s[1])
    else:
        d[s[0] + " " + s[1]] = d.get(s[0] + " " + s[1], 0) + int(s[2])
for k, v in d.items():
    print(k, v)