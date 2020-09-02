from itertools import combinations_with_replacement as combr

s = input().split()
l = list(combr(s[0], int(s[1])))

ans = []

for i in l:
    ans.append(''.join(sorted(i)))

ans.sort()
for i in ans:
    print(i)
