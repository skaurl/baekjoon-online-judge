import sys
n = int(sys.stdin.readline())
for i in range(n):
    k = sys.stdin.readline().split()
    m = list(k[1])
    l = ''
    for j in range(len(m)):
        l += m[j]*int(k[0])
    print(l)