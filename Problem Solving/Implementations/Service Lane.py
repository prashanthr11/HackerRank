n, m = map(int, input().split())
l = list(map(int, input().split()))
for i in range(m):
    x, y = map(int, input().split())
    print(min(l[x:y + 1]))
