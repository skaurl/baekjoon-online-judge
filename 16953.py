import sys
from collections import deque

a,b = map(int, sys.stdin.readline().strip().split())
ans = -1
que = deque([(a,1)])
while que:
    i, cnt = que.popleft()
    if i == b:
        ans = cnt
        break
    if i*2 <= b:
        que.append((i*2,cnt+1))
    if int(str(i)+'1') <= b:
        que.append((int(str(i)+'1'), cnt+1))
print(ans)