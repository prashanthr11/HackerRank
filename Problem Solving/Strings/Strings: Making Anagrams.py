
from collections import Counter

n = map(str, input())
m = map(str, input())
d = Counter(n)
d2 = Counter(m)
x = (d - d2).values()
y = (d2 - d).values()
print(sum(x) + sum(y))

