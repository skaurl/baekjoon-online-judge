import sys

n = int(sys.stdin.readline().strip())
a, b = 1, 0
for i in range(n):
    a, b = (a+b)%10, a%10
print(a)