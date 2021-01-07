import sys
M,N = map(int,sys.stdin.readline().strip().split())
lst = [list(sys.stdin.readline().strip()) for i in range(M)]
A = [["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"],["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"]]
ans = [[0]*(N-7) for i in range(M-7)]
for i in range(M-7):
    for j in range(N-7):
        cnt = 0
        tmp = [k[j:j+8] for k in lst[i:i+8]]
        for a in range(len(tmp)):
            for b in range(len(tmp[a])):
                if tmp[a][b] != A[a][b]:
                    cnt+=1
        ans[i][j]=min(cnt,64-cnt)
ans = [min(i) for i in ans]
print(min(ans))