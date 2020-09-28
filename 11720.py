import sys
n = sys.stdin.readline()
n = sys.stdin.readline()
n = list(n)
del n[-1]
for i in range(len(n)):
    n[i] = int(n[i])
print(sum(n))