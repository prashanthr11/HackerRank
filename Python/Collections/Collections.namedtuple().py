from collections import namedtuple

n = int(input())
l = list(input().split())
x = namedtuple('student', [i for i in l])

sumi = 0
for i in range(n):
    s = list(input().split())
    t = x(*s)
    sumi += int(t.MARKS)

print('{0:.2f}'.format(sumi / n))
