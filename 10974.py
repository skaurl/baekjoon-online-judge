from itertools import permutations
n = int(input())
for i in list(permutations(range(1,n+1),n)):
    print(*i)