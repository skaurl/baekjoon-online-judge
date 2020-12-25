from itertools import combinations

N,M=map(int,input().split())
A = sorted(list(map(int, input().split())))
A = list(combinations(A,M))
A = sorted(list(set(A)))

for i in A:
    print(' '.join(map(str, i)))