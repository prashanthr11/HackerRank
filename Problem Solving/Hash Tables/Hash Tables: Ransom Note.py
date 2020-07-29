from collections import Counter

n, m = map(int, input().split())
s1 = Counter(list(input().split()))
s2 = Counter(list(input().split()))
if len(s2 - s1):
    print('No')
else:
    print('Yes')

