import sys
n = int(sys.stdin.readline())
N = []
for i in range(n):
    a = sys.stdin.readline().split()
    a.insert(1,i)
    a[0] = int(a[0])
    N.append(tuple(a))
N.sort(key = lambda x:(x[0],x[1]))
for i in range(len(N)):
    print(N[i][0],N[i][2])