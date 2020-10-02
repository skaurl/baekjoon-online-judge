import sys
n = int(sys.stdin.readline())
N = []
for i in range(n):
    a = sys.stdin.readline().split()
    N.append([int(a[0]),int(a[1])])
N = sorted(N)
for i in N:
    print(i[0],i[1])