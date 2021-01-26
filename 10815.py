import sys

a = int(sys.stdin.readline().strip())
A = {i:1 for i in list(map(int,sys.stdin.readline().strip().split()))}
b = int(sys.stdin.readline().strip())
B = list(map(int,sys.stdin.readline().strip().split()))
for i in range(len(B)):
    try:
        print(A[B[i]],end=" ")
    except:
        print(0,end=" ")