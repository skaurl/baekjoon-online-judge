import sys
n,m = map(int,sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().split()))
result = [0]
for i in range(n):
    result.append(result[-1]+lst[i])
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    if a!=1:
        print(result[b]-result[a-1])
    else:
        print(result[b])