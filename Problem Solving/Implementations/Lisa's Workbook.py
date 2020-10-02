
def solve(l, m):
    ret = list()

    for i in l:
        x = 1
        while x + m <= i:
            tmp = list()

            for j in range(x, x + m):
                tmp.append(j)
            x += m
            ret.append(tmp)

        qw = list()
        for j in range(x, i + 1):
            qw.append(j)
        ret.append(qw)

    return ret

n, m = map(int, input().split())
l = list(map(int, input().split()))
ans = solve(l, m)

cnt = 0
for i in range(len(ans)):
    if i + 1 in ans[i]:
        cnt += 1

print(cnt)

