import sys
n = int(sys.stdin.readline())
N = []
for i in range(n):
    m = sys.stdin.readline().split()
    for j in range(len(m)):
        m[j] = int(m[j])
    N.append(m[1:])
for i in range(len(N)):
    avg = sum(N[i])/len(N[i])
    k = 0
    for j in range(len(N[i])):
        if N[i][j] > avg:
            k += 1
    print('%0.3f%%' % round(k/len(N[i])*100,3))