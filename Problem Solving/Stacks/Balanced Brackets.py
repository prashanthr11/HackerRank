open_braces = ["{", "[", "("]
for i in range(int(input())):
    lst = list()
    flag = True
    l = list(map(str, input()))
    for i in l:
        if i in open_braces:
            lst.append(i)
        if len(lst) == 0:
            flag = False
            break
        elif i == "]":
            if lst[-1] == "[":
                lst.pop()
            else:
                flag = False
                break
        elif i == ")":
            if lst[-1] == "(":
                lst.pop()
            else:
                flag = False
                break
        elif i == "}":
            if lst[-1] == "{":
                lst.pop()
            else:
                flag = False
                break
    if len(lst):
        flag = False
    if flag:
        print("YES")
    else:
        print("NO")
