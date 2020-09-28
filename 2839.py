import sys
n = int(sys.stdin.readline())
N = []
for x in range((n//3)+1):
    for y in range((n//5)+1):
        if 3*x+5*y == n:
            N.append(x+y)
if len(N) == 0:
    print(-1)
else:
    print(min(N))