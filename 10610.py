import sys

n = sys.stdin.readline().strip()

if '0' in n and sum([int(i) for i in n])%3 == 0:
    print(int("".join(sorted(list(n),reverse=True))))
else:
    print(-1)