import sys
n = int(sys.stdin.readline())
N = list(map(int, sys.stdin.readline().split()))
print(max(N)*min(N))