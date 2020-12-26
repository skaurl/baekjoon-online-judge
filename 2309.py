from itertools import combinations

A = []

for i in range(9):
    A.append(int(input()))

B = list(combinations(A,7))

for i in B:
    if sum(i) == 100:
        c = i
        break

c = sorted(c)

for i in c:
    print(i)