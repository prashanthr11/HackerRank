n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    st = list(input().split())
    if(st[0] == "intersection_update"):
        a = set(map(int, input().split()))
        s &= a
    if(st[0] == "update"):
        a = set(map(int, input().split()))
        s |= a
    if(st[0] == "symmetric_difference_update"):
        a = set(map(int, input().split()))
        s ^= a
    if(st[0] == "difference_update"):
        a = set(map(int, input().split()))
        s -= a
print(sum(s))
