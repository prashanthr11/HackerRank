n = int(input())
l = [0 for i in range(100)]
q = list(map(int, input().split()))

for i in q:
    l[i] += 1

for i in l:
    print(i, end = ' ')
