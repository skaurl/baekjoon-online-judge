import sys
from collections import Counter

n,c = map(int, sys.stdin.readline().strip().split())
lst = list(map(int, sys.stdin.readline().strip().split()))

tmp = []

for i in Counter(lst).most_common():
    tmp.append([i[0],i[1],lst.index(i[0])])

tmp = sorted(tmp,key=lambda x : (x[1], -x[2]),reverse=True)

ans = []

for i in tmp:
    for j in range(i[1]):
        ans.append(i[0])

print(*ans)