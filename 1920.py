n = int(input())
N = list(map(int,input().split()))
m = int(input())
M = list(map(int,input().split()))

A = {}

for i in N:
    A[i]=1

for i in M:
    if i in A:
        print(1)
    else:
        print(0)