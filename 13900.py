import sys

num = int(sys.stdin.readline().strip())

lst = list(map(int,sys.stdin.readline().strip().split()))

print((sum(lst)**2 - sum([i**2 for i in lst]))//2)