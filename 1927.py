import sys
import heapq

n = int(sys.stdin.readline())
array = []

heapq.heapify(array)

for _ in range(n):
    a = int(sys.stdin.readline())
    if a==0:
        try:
            print(heapq.heappop(array))
        except:
            print(0)
    else:
        heapq.heappush(array,a)