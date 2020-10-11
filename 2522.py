import sys
N = int(sys.stdin.readline())
A = []
for i in range(N):
    A.append(' '*(N-i-1)+'*'*(i+1))
for i in range(len(A)):
    print(A[i])
for i in range(len(A)-1):
    print(A[N-i-2])