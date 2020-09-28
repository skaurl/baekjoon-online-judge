import sys
N = []
for i in range(9):
    n = sys.stdin.readline()
    N.append(int(n))
for i in range(len(N)):
    if N[i] == max(N):
        print(N[i])
        print(i+1)