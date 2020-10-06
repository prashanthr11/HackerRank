for i in range(int(input())):
    a, k = map(int, input().split())

    maxi = 0

    print(k - 1 if (k - 1) | k <= a else k - 2)

