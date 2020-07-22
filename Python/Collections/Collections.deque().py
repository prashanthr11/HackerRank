from collections import deque

l = deque()
for i in range(int(input())):
    s = list(map(str, input().split()))
    if len(s) == 2:
        if s[0] == "append":
            l.append(s[1])
        if s[0] == "appendleft":
            l.appendleft(s[1])
    else:
        if s[0] == "pop":
            l.pop()
        else:
            l.popleft()

print(*l)

