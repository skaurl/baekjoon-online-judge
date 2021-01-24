import sys

a,b = map(int,sys.stdin.readline().strip().split())
lst_1 = list(map(int,sys.stdin.readline().strip().split()))
lst_2 = list(map(int,sys.stdin.readline().strip().split()))
print(*sorted(lst_1+lst_2))
