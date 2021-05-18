import sys

num = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst.sort(reverse=True)

ans = []

for i,j in enumerate(lst):
    ans.append(i+j+2)

print(max(ans))