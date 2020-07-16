from collections import defaultdict
n =int(input())
d = defaultdict(int)

for i in range(n):
    a, b = input().split()
    d[a] = b

for i in range(n):
    k = input()
    if(d[k]):
        print(k + "=" + d[k])
    else:
        print("Not found")

