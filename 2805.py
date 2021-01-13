import sys
a,b = map(int, sys.stdin.readline().strip().split())
lst = list(map(int, sys.stdin.readline().strip().split()))
start = 0
end = max(lst)

while start<=end:
    mid = (start+end)//2
    ans = 0
    for i in range(len(lst)):
        if mid<lst[i]:
            ans += lst[i]-mid
    if ans >= b:
        start = mid + 1
    else:
        end = mid - 1
print(end)