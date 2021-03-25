import sys

S = sys.stdin.readline()
tmp = ''
ans = ''

tag = False

for i in S:
    if i == '<':
        tag = True
        ans += tmp[::-1] + '<'
        tmp = ''
    elif i == '>':
        tag = False
        ans += '>'
    elif i == ' ':
        if tag:
            ans += ' '
        else:
            ans += tmp[::-1] + ' '
            tmp = ''
    else:
        if tag:
            ans += i
        else:
            tmp += i

ans += tmp[::-1][1:]
print(ans)