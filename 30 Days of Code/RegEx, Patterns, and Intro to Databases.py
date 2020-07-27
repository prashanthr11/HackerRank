ans = list()
for i in range(int(input())):
    f, e = map(str, input().split())
    if e.endswith("@gmail.com"):
        ans.append(f)

for i in sorted(ans):
    print(i)
