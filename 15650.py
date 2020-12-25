from itertools import combinations

N, M = map(int, input().split())

A = combinations(range(1,N+1),M)

for i in A:
    print(' '.join(map(str, i)))