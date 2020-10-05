class Trie:
    def __init__(self, l = list(), ch = None):
        self.l = [ch for i in range(11)]

    def add(self, root, s):
        head = root
        issubstr = False
        s += '$'
        for i in range(len(s)):
            if s[i] == '$':
                x2 = ['$' for i in range(11)]
                head.l = x2
                return issubstr
            else:
                if head.l[ord(s[i]) - ord('a')] == '$':
                    issubstr = True
                    return issubstr
                else:
                    if head.l[ord(s[i]) - ord('a')]:
                        head = head.l[ord(s[i]) - ord('a')]
                        issubstr = True
                    else:
                        x2 = Trie()
                        issubstr = False
                        head.l[ord(s[i]) - ord('a')] = x2
                        head = x2                
        head = root
        return issubstr


if __name__ == '__main__':
    root = Trie()
    flag = True
    for i in range(int(input())):
        ip = input()
        if root.add(root, ip):
            flag = False
            break
    if not flag:
        print('BAD SET')
        print(ip)
    else:
        print("GOOD SET")
