from itertools import permutations

n = int(input())
m = list(map(int,input().split()))
A = []
for i in list(permutations(m,n)):
    result = 0
    for j in range(1,len(i)):
        result += abs(i[j-1]-i[j])
        A.append(result)
print(max(A))