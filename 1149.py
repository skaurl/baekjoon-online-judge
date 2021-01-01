n = int(input())
N = []
for i in range(n):
    N.append(list(map(int,input().split())))
for i in range(1,len(N)):
    N[i][0] = min(N[i-1][1],N[i-1][2]) + N[i][0]
    N[i][1] = min(N[i-1][0],N[i-1][2]) + N[i][1]
    N[i][2] = min(N[i-1][0],N[i-1][1]) + N[i][2]
print(min(N[-1]))