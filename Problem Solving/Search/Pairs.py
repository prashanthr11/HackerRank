from collections import Counter

n, m = map(int, input().split())
l = list(map(int, input().split()))
d = Counter(l)
i = 0
ans = 0

while i < len(l):
    if d[m + l[i]]:
        ans += 1
    i += 1

print(ans)
