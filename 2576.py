import sys

N = []

for i in range(7):
    a = int(sys.stdin.readline())
    if a%2==1:
        N.append(a)

if len(N) == 0:
    print(-1)
else:
    print(sum(N))
    print(min(N))