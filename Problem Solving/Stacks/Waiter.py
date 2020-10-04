def isprime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_numbers(n):
    i, cnt = 0, 2
    l = list()
    while i < n:
        if isprime(cnt):
            l.append(cnt)
            i += 1
        cnt += 1
    return l


def solve(l, pr):
    for i in pr:
        b = list()
        a = list()
        for j in l[::-1]:
            if not j % i:
                b.append(j)
            else:
                a.append(j)
        for i in b[::-1]:
            print(i)
        l = a
    for i in a[::-1]:
        print(i)

n, m = map(int, input().split())
ls = list(map(int, input().split()))
l = prime_numbers(m)
# ls.reverse()
solve(ls, l)
