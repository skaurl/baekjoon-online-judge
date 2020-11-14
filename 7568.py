import sys

n = int(sys.stdin.readline())

N = []

for i in range(n):
    N.append(list(map(int,sys.stdin.readline().split())))

for i in N:
    rank = 1
    for j in N:
        if (i[0] != j[0]) & (i[1] != j[1]):
            if (i[0] < j[0]) & (i[1] < j[1]):
                rank += 1
    print(rank,end=" ")