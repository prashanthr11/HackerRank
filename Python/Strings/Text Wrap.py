import textwrap

def wrap(string, max_width):
    i = 0
    s = ""
    while i < len(string):
        s += string[i:i + max_width] + '\n'
        i += max_width
    return s[:-1]

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
