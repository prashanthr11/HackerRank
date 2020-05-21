from collections import Counter
n = int(input())
l = Counter(map(str, input().split()))
t = int(input())
cnt = 0
for i in range(t):
    s, p = list(map(str, input().split()))
    if l[s]:
        cnt += int(p)
        l[s] -= 1
print(cnt)