import sys
n = int(sys.stdin.readline())
N = []
for i in range(n):
    N.append(int(sys.stdin.readline()))

for i in sorted(N):
    print(i)