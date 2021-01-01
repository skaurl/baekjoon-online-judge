n = int(input())
N = list(map(int,input().split()))
M = [0]*n
for i in range(1,n+1):
    cnt = 0
    for j in range(n):
        if cnt==N[i-1] and M[j]==0:
            M[j] = i
            break
        elif M[j]==0:
            cnt+=1
print(*M)