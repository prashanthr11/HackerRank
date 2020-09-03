def minion_game(s):
    l = set('AEIOU')
    stuart, kevin = 0, 0
    ln = len(s)
    for i in range(ln):
        if s[i] not in l:
            stuart += ln - i
        else:
            kevin += ln - i

    if stuart > kevin:
        print("Stuart {}".format(stuart))
    elif stuart < kevin:
        print("Kevin {}".format(kevin))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
