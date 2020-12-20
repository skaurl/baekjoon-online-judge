N, M = map(int, input().split())
visit = [False]*N
out = []

def dfs(depth,N,M):
    if depth == M:
        print(' '.join(map(str, out)))
    for i in range(len(visit)):
        if not visit[i]:
            visit[i] = True
            out.append(i+1)
            dfs(depth+1,N,M)
            visit[i] = False
            out.pop()

dfs(0,N,M)