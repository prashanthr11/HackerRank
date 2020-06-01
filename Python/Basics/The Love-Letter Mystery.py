import string
lc = " "
lc += string.ascii_lowercase
n = int(input())
for i in range(n):
    cnt = 0
    l = list(map(str, input()))
    if len(l) % 2 != 0:
        for i in range(len(l) // 2):
            if l[i] != l[len(l) - 1 - i]:
                cnt += abs(lc.find(l[i]) - lc.find(l[len(l) - 1 - i]))
    else:
        for i in range(len(l) // 2):
            if l[i] != l[len(l) - 1 - i]:
                cnt += abs(lc.find(l[i]) - lc.find(l[len(l) - 1 - i]))
    print(cnt)
