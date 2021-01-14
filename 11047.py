import sys

a,b = map(int,sys.stdin.readline().strip().split())
lst = []
for i in range(a):
    lst.append(int(sys.stdin.readline().strip()))
lst = sorted(lst,reverse=True)
ans = 0
for i in range(len(lst)):
    if b == 0:
        break
    if lst[i] <= b:
        ans += b//lst[i]
        b = b%lst[i]
    else:
        pass
print(ans)