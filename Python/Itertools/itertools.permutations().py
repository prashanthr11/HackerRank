from itertools import permutations


s, l = list(map(str, input().split()))
q = list(permutations(s, int(l)))

ans = list()
for i in q:
    ans.append(''.join(i))
ans.sort()
for i in ans:
    print(i)
