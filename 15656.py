from itertools import product

N,M=map(int,input().split())
A = sorted(list(map(int, input().split())))

_list = []

for i in range(M):
    _list.append(A)

B = list(product(*_list))

for i in B:
    print(' '.join(map(str, i)))