import sys
n = int(sys.stdin.readline())
N = []
for i in range(n):
    N.append(sys.stdin.readline()[:-1])
N = list(set(N))
for i in range(len(N)):
    N[i] = [len(N[i]),N[i]]
N = sorted(N)
for i in range(len(N)):
    print(N[i][1])