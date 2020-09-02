from itertools import combinations as com

n = int(input())
l = input().replace(' ', '')
k = int(input())

l = list(com(l, k))
cnt = 0

for i in l:
    if 'a' in i:
        cnt += 1

print("{0:.3f}".format(cnt / len(l)))
