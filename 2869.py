import sys
import math
n = sys.stdin.readline().split()
A = int(n[0])
B = int(n[1])
V = int(n[2])
print(math.ceil((V-B)/(A-B)))