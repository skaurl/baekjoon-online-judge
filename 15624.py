import sys
n = int(sys.stdin.readline())
N = [0,1]
for i in range(n):
    N.append((N[i]+N[i+1])%1000000007)
print(N[n])