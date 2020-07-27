n, l = int(input()), list(map(int, input().split()))
l = [int(i) for i in l]

if min(l) < 0:
    print(False)
    exit()

l2 = [str(i) for i in l]
flag = False

for i in l2:
    if i == i[::-1]:
        flag = True
        break
print(flag)

