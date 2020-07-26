s = input()
ans = list()
cnt, i = 1, 1

while i < len(s):
    if s[i] == s[i - 1]:
        i += 1
        cnt += 1
    else:
        ans.append((cnt, int(s[i - 1])))
        cnt = 1
        i += 1

if s[i - 1] == s[i - 2]:
    ans.append((cnt, int(s[i - 1])))
else:
    ans.append((1, int(s[i - 1])))
for i in ans:
    print(i, end = " ")
