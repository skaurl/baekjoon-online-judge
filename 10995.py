import sys
N = int(sys.stdin.readline())

for i in range(N):
    if i%2 == 0:
        print('*'+' *'*(N-1))
    else:
        print(' *'*N)