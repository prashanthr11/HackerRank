n = int(input())
l = list(map(int, input().split()))

ans = list()
for i in range(1, n + 1):
    ans.append(l.index(i) + 1)

for i in ans:
    print(l.index(i) + 1)
