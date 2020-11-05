import sys
n_1 = list(map(int,sys.stdin.readline().split()))
n_2 = list(map(int,sys.stdin.readline().split()))
n_3 = list(map(int,sys.stdin.readline().split()))

ccw = ( n_1[0]*n_2[1] + n_2[0]*n_3[1] + n_3[0]*n_1[1] ) - ( n_1[1]*n_2[0] + n_2[1]*n_3[0] + n_3[1]*n_1[0] )

if ccw > 0:
    print(1)
elif ccw < 0:
    print(-1)
else:
    print(0)