import sys

total = int(sys.stdin.readline())
N = []
for i in range(9):
    N.append(int(sys.stdin.readline()))
print(total-sum(N))