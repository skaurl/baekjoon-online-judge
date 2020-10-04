import sys
N = int(sys.stdin.readline())
A = []
for i in range(2*N-1):
    A.append(' ')
x = ''
for i in range(N):
    x = ''
    A[N-1+i] = '*'
    A[N-1-i] = '*'
    for j in range(len(A)):
        x += A[j]
    print(x.rstrip())
