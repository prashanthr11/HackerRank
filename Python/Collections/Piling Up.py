for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    maxi = max(l)
    if maxi == l[0] or maxi == l[-1]:
        print('Yes')
    else:
        print('No')

