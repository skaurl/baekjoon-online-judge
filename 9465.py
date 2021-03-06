import sys

n = int(sys.stdin.readline().strip())
for i in range(n):
    m = int(sys.stdin.readline().strip())
    tmp = []
    for j in range(2):
        tmp.append(list(map(int,sys.stdin.readline().strip().split())))
    tmp[0][1] += tmp[1][0]
    tmp[1][1] += tmp[0][0]
    for j in range(2,m):
        tmp[0][j] += max(tmp[1][j-1],tmp[1][j-2])
        tmp[1][j] += max(tmp[0][j-1],tmp[0][j-2])
    print(max(tmp[0][m-1],tmp[1][m-1]))