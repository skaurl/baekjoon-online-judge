from itertools import combinations

N,M=map(int,input().split())
A = sorted(list(map(int, input().split())))

for i in combinations(range(N),M):
    B = []
    for j in i:
        B.append(A[j])
    print(' '.join(map(str, B)))