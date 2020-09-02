from itertools import combinations as comb


s, l = list(map(str, input().split()))
q = list()

for i in range(1, int(l) + 1):
    q.append(list(comb(s, i)))

ans = list()
for i in q:
    for j in i:
            ans.append(''.join(sorted(j)))

ans.sort()
ans.sort(key = lambda x: len(x))

for i in ans:
    print(i)
