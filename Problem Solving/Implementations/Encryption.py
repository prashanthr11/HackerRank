from math import floor as fl, ceil as cl, sqrt as st
import textwrap

s = input().replace(' ', '')

ln = len(s)
mini, maxi = fl(st(ln)), cl(st(ln))

s = textwrap.wrap(s, width = maxi)

i = 0

ans = ''
while i < maxi:
    j = 0
    while j < maxi:
        try:
            ans += s[j][i]
        except IndexError:
            pass
        j += 1
    ans += ' '
    i += 1

print(ans)
