import sys
import math
n = sys.stdin.readline().split()
A = int(n[0])
B = int(n[1])
C = int(n[2])
if C-B > 0:
    print(math.floor(A/(C-B)+1))
else:
    print(-1)