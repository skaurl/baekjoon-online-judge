import sys
a,b = map(int,sys.stdin.readline().strip().split())
lst = sorted(list(map(int,sys.stdin.readline().strip().split())))
print(lst[b-1])