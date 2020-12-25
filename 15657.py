from itertools import combinations_with_replacement

N,M=map(int,input().split())
A = sorted(list(map(int, input().split())))

for i in combinations_with_replacement(range(N),M):
    B = []
    for j in i:
        B.append(A[j])
    print(' '.join(map(str, B)))