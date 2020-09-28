import sys
n = sys.stdin.readline()
N = sys.stdin.readline().split()
for i in range(len(N)):
    N[i] = int(N[i])
print(min(N),max(N))