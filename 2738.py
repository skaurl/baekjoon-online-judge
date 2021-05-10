import sys

N, M = map(int, sys.stdin.readline().split())
a = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    b = list(map(int, input().split()))
    for j in range(M):
        print(a[i][j]+b[j], end=' ')
    print()