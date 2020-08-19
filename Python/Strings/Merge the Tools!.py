from collections import defaultdict

def merge_the_tools(s, k):
    if len(s) % k == 0:
        cnt = 0
        l = list()
        st = ""
        for i in s:
            if cnt == k:
                l.append(st)
                cnt = 1
                st = i
            else:
                st += i
                cnt += 1
        l.append(st)
        
        for i in l:
            d = defaultdict(int)
            ret = ""
            for j in i:
                if d[j] == 0:
                    ret += j
                d[j] += 1
            print(ret)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
