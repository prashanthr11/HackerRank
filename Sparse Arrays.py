n = int(input())
l = list()
for i in range(n):
    s = input()
    l.append(s)


n2 = int(input())
l2 = list()
for i in range(n2):
    s = input()
    l2.append(l.count(s))
    

for i in l2:
    print(i)
