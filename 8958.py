import sys
n = int(sys.stdin.readline())
N = []
for i in range(n):
    m = sys.stdin.readline()
    N.append(m)
for i in range(len(N)):
    k = 0
    sum = 0
    for j in range(len(N[i])):
        if N[i][j] == 'O':
            k += 1
        else:
            k = 0
        sum += k
    print(sum)