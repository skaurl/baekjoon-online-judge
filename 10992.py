import sys
N = int(sys.stdin.readline())
for i in range(N):
    if i == 0:
        print(' '*(N-i-1)+'*')
    elif i == N-1:
        print('*'*(2*N-1))
    else:
        print(' '*(N-i-1)+'* '+'  '*(i-1)+'*')