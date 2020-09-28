import sys
n = int(sys.stdin.readline())
m = 1
for i in range(n):
    m *= (i+1)
print(m)