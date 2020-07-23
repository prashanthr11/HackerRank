from collections import Counter

s = input()
d = Counter(s)
cnt = 0

d = dict(sorted(d.items()))

for k, v in sorted(d.items(), key=lambda x:x[1], reverse=True):
    print(k, v)
    cnt += 1
    if cnt == 3:
        break
