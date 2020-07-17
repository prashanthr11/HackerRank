def check(l1, l2):
    d1, m1, y1 = map(int, l1)
    d2, m2, y2 = map(int, l2)
    if y2 > y1:
        return 0

    if y2 < y1:
        return 10000

    if m2 < m1:
        return abs(m2 - m1) * 500

    if m2 > m1:
        return 0

    if d2 < d1:
        return abs(d2 - d1) * 15
    
    return 0
    
d1 = list(map(int, input().split()))
d2 = list(map(int, input().split()))
print(check(d1, d2))
