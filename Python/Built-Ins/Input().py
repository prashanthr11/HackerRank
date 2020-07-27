a, b = map(int, input().split())
s = input().replace('x', str(a)).split('+')
x = 0
for i in s:
    x += eval(i)
if x == b:
    print(True)
else:
    print(False)

