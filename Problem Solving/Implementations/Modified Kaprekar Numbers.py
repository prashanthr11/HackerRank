def iskaprekar(a):
    ln = len(str(a))
    st = str(a ** 2)
    ln2 = len(st)
    
    while True:
        if ln2 == (2 * ln) or ln2 == (2 * ln) - 1:
            r, l = 0, 0
            if len(st[ln2 - ln:]):
                r = int(st[ln2 - ln:])
            x = st[:ln2 - ln]
            if len(x):
                l = int(x)

            if l + r == a:
                return True
            else:
                return False
        else:
            st = str(a ** 4)
            ln2 = len(st)

    return False

def solve(a, b):
    ret = list()
    for i in range(a, b + 1):
        if iskaprekar(i):
            ret.append(i)
    return ret



n = int(input())
m = int(input())
ans = solve(n, m)
if len(ans):
    print(*ans)
else:
    print('INVALID RANGE')

