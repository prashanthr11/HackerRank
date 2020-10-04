l = list()
tmp = ''

for i in range(int(input())):
    s = input().split()
    if len(s) > 1:
        a = int(s[0])
        if a == 1:
            tmp += s[1]
            l.append(tmp)
        elif a == 2:
            b = int(s[1])
            tmp = tmp[:-b]
            l.append(tmp)
        elif a == 3:
            b = int(s[1])
            print(tmp[b - 1])
    else:
        l.pop()
        if len(l):
            tmp = l[-1]
        else:
            tmp = ''
