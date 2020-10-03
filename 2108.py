import sys
from collections import Counter
n = int(sys.stdin.readline())
N = []
for i in range(n):
    N.append(int(sys.stdin.readline()))

N = sorted(N)

print(round(sum(N)/len(N)))

print(N[n//2])

k=Counter(N).most_common()

if len(N) > 1:
    if k[0][1] == k[1][1]:
        print(k[1][0])
    else :
        print(k[0][0])
else :
    print(N[0])

print(N[-1]-N[0])