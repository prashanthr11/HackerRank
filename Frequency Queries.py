n = int(input())
d = dict()
flag = False
for i in range(n):
    l = input().split()
    t = int(l[0])
    a = int(l[1])
    if t == 1:
        d[a] = d.get(a, 0) + 1
    if t == 2:
        d[a] = d.get(a, 0) - 1
    if t == 3:
        for k in d:
            if d[k] == a:
                flag = True
                break
            else:
                flag = False
        if flag:
            print("1")
        else:
            print("0")
