import sys

n = int(sys.stdin.readline().strip())
N = [[0]*10 for i in range(n)]
N[0] = [0]+[1]*9

for i in range(1,n):
    for j in range(len(N[i])):
        if j == 0:
            N[i][j] = N[i-1][1]
        elif j == 9:
            N[i][j] = N[i-1][8]
        else:
            N[i][j] = N[i-1][j-1]+N[i-1][j+1]

print(sum(N[n-1])% 1000000000)