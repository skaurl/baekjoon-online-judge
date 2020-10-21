import sys
N = int(sys.stdin.readline())
for i in range(N):
    if N%2==0:
        print('*'+' *'*(int(N/2)-1))
        print(' *'*(int(N/2)))
    else:
        print('*'+' *'*(int(N/2)))
        print(' *'*(int(N/2)))