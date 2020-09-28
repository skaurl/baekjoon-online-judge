import sys
n1 = int(sys.stdin.readline())
n2 = int(sys.stdin.readline())
n3 = int(sys.stdin.readline())
n = n1*n2*n3
n = str(n)
n = list(n)
N = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(n)):
    for j in range(0,10,1):
        if int(n[i]) == j:
            N[j] += 1
for i in range(len(N)):
    print(N[i])