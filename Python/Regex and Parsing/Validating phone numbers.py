l = ['7','8','9']

for i in range(int(input())):
    s = input()
    try:
        if s[0] in l and len(s) == 10 and int(s):
            print('YES')
        else:
            print('NO')
    except:
        print('NO')
