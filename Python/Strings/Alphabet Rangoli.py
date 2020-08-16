def print_rangoli(size):
    from string import ascii_lowercase

    lc = list (ascii_lowercase) 
    n = size

    l = list()
    cnt = 2
    step = n
    for i in range(n):
        s = '-' * ((2 * n) - cnt)
        for i in range(n - 1, step - 2, -1):
            s += lc[i] + '-'
        for i in range(step, n):
            s += lc[i] + '-'
        
        s += '-' * ((2 * n) - cnt)
        cnt += 2
        step -= 1
        l.append(s[:-1])
        
    step += 1
    cnt -= 2
    for i in range(n):
        s = '-' * ((2 * n) - cnt)
        for i in range(n - 1, step - 2, -1):
            s += lc[i] + '-'
        for i in range(step, n):
            s += lc[i] + '-'
        
        s += '-' * ((2 * n) - cnt)
        cnt -= 2
        step += 1
        l.append(s[:-1])
    l.pop(len(l) // 2)
    for i in l:
        print(i)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
