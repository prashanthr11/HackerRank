n = int(input())
s = set(map(int, input().split()))
q = int(input())
for i in range(q):
    a = list(map(str, input().split()))
    if len(a) > 1:
        s.discard(int(a[1]))
    else:
        s.pop()

print(sum(s))
