import string

cnt = 0
def count_substring(string, sub_string):
    global cnt
    le = len(sub_string)
    j = le
    for i in range(0, len(string)):
        if string[i:j] == sub_string:
            cnt += 1
        j += 1
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)