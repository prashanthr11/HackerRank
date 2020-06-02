if __name__ == '__main__':
    d = dict()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        d[score] = d.get(score, list()) +[name]
    del d[min(d)]
    for i in sorted(list(d[min(d)])):
        print(i)
