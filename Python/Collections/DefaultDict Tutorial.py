from collections import defaultdict

d = defaultdict(list)

n, m = map(int, input().split())

for i in range(n):
    s = input()
    d[s].append(i + 1)

for i in range(m):
    s = input()
    if len(d[s]):
        print(*d[s])
    else:
        print(-1)

