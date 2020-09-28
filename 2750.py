import sys
n = int(sys.stdin.readline())
N = []
for i in range(n):
    m = int(sys.stdin.readline())
    N.append(m)
N = sorted(N)
for i in range(len(N)):
    print(N[i])