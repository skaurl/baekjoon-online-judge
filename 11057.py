import sys

n = int(sys.stdin.readline().strip())

N = [[1]*10] + [[0]*10 for i in range(999)]

for i in range(1,1000):
    for j in range(10):
        for k in range(j+1):
            N[i][j] += N[i-1][k]

print(sum(N[n-1])%10007)