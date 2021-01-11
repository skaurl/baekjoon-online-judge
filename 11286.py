import sys
import heapq
n = int(sys.stdin.readline().strip())
heap = []
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num != 0:
        heapq.heappush(heap,(abs(num),num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)