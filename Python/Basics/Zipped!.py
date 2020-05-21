n, m = map(int, input().split())
d = dict()
for i in range(m):
    s = list(map(float, input().split()))
    for i in range(len(s)):
        d[i] = d.get(i, 0) + s[i]

for k, v in d.items():
    print(d[k]/m)