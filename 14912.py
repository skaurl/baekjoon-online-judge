import sys
from collections import Counter

n, d = map(int, sys.stdin.readline().strip().split())

tmp = []

for i in range(1,n+1):
    tmp.extend(list(str(i)))

print(Counter(tmp)[str(d)])