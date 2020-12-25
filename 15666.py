from itertools import combinations_with_replacement

N,M=map(int,input().split())
A = sorted(list(map(int, input().split())))
A = list(combinations_with_replacement(A,M))
A = sorted(list(set(A)))

for i in A:
    print(' '.join(map(str, i)))