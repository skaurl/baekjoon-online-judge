import sys
N = int(sys.stdin.readline())
A = []
for i in range(2*N-1):
    A.append(' ')
X = []
x = ''
for i in range(N):
    x = ''
    A[N-1+i] = '*'
    A[N-1-i] = '*'
    for j in range(len(A)):
        x += A[j]
    X.append(x.rstrip())
for i in range(len(X)):
    print(X[len(X)-i-1])
for i in range(len(X)-1):
    print(X[i+1])