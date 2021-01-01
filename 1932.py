n = int(input())
N = []
for i in range(n):
    N.append(list(map(int,input().split())))
for i in range(1,len(N)):
    for j in range(len(N[i])):
        if j==0:
            N[i][j] += N[i-1][j]
        elif i==j:
            N[i][j] += N[i-1][j-1]
        else:
            N[i][j] = max(N[i][j]+N[i-1][j-1],N[i][j]+N[i-1][j])
print(max(N[-1]))