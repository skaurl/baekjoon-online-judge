import sys
n = int(sys.stdin.readline().strip())
i = 1
while i * (i+1) / 2 <= n:
    i+=1
print(i-1)