import sys
n = int(sys.stdin.readline())
N = []
for i in range(1,65,1):
    N.append((2**i-1)*(2**(64-i)))

print(N.index(n)+1)