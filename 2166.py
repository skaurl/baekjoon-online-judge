n = int(input())
N = []
for i in range(n):
    N.append(list(map(int,input().split())))
N.append(N[0])
ans = 0
for i in range(n):
    ans+=N[i][0]*N[i+1][1]
    ans-=N[i+1][0]*N[i][1]
print(round(0.5*abs(ans),1))