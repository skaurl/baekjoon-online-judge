import sys
from collections import deque

n = int(sys.stdin.readline().strip())
queue = deque([])
for i in range(n):
    N = sys.stdin.readline().strip()
    if N[:4] == "push":
        N = N.split()
        queue.append(int(N[1]))
    elif N == "pop":
        try:
            print(queue.popleft())
        except:
            print(-1)
    elif N == "size":
        print(len(queue))
    elif N == "empty":
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif N == "front":
        try:
            print(queue[0])
        except:
            print(-1)
    elif N == "back":
        try:
            print(queue[-1])
        except:
            print(-1)