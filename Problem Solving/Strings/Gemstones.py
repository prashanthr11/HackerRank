from collections import Counter
d = Counter()
n = int(input())
for i in range(n):
    l = set(list(map(str, input())))
    d += Counter(l)
cnt = 0
for k, v in d.items():
    if v == n:
        cnt += 1
print(cnt)
