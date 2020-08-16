n, m = map(int, input().split())
l = list()
pt = ".|."
cnt = 1
yt = m // 2 - 1
for i in range(n // 2):
    s = ''
    for j in range(yt):
        s += '-'
    s += pt * cnt
    for j in range(yt):
        s += '-'
    cnt += 2
    yt -= 3
    l.append(s)
l.append('-' * (m // 2 - 3) + "WELCOME" + '-' * (m // 2 - 3))
yt = 3
cnt -= 2
for i in range(n // 2):
    s = ''
    for j in range(yt):
        s += '-'
    s += pt * cnt
    for j in range(yt):
        s += '-'
    cnt -= 2
    yt += 3
    l.append(s)
for i in l:
    print(i)

