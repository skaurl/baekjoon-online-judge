import sys
N = []
for i in range(10):
    n = int(sys.stdin.readline())
    N.append(n)
for i in range(len(N)):
    N[i] = N[i]%42
N = list(set(N))
print(len(N))