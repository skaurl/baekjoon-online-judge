from itertools import product
N, M = map(int, input().split())
X = "123456789"[:N]
_list = []
for i in range(M):
    _list.append(X)
pd = list(product(*_list))
for i in pd:
    print(' '.join(map(str, i)))