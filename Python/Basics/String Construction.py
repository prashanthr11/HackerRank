# n = int(input())
# for i in range(n):
#     cnt = 0
#     s = input()
#     p = ''
#     for i in s:
#         if i not in p:
#             cnt += 1
#         p += i
#     print(cnt)


#2nd Method

for i in range(int(input())):
    print(len(set(input())))
