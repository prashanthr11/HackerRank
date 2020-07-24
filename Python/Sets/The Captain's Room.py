from collections import Counter

n = int(input())
l = list(map(int, input().split()))
d = Counter(l)

for k, v in d.items():
    if v == 1:
        print(k)
        break
