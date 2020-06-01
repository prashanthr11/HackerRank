n = int(input())
for i in range(n):
    cnt = 0
    l = list(map(str, input()))
    for i in range(1, len(l)):
        if l[i] == l[i - 1]:
            cnt += 1
    print(cnt)