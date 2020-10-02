def solve(a, b, c):
    cho = a // b
    cnt = cho
    while cho >= c:
        cho -= c
        cho += 1
        cnt += 1
    return cnt


for i in range(int(input())):
    a, b, c = map(int, input().split())
    print(solve(a, b, c))
