from itertools import permutations

N,M=map(int,input().split())
A = list(map(int, input().split()))
A = list(permutations(A,M))
A = sorted(list(set(A)))

for i in A:
    print(' '.join(map(str, i)))