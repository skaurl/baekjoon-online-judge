import sys
N = []
N.append(int(sys.stdin.readline()))
N.append(int(sys.stdin.readline()))
N.append(int(sys.stdin.readline()))
N.append(int(sys.stdin.readline()))
N.append(int(sys.stdin.readline()))

for i in range(len(N)):
    if N[i] <= 40:
        N[i] = 40

print(sum(N)//len(N))