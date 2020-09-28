import sys
n = int(sys.stdin.readline())
n = sys.stdin.readline().split()
for i in range(len(n)):
    n[i] = int(n[i])
m = max(n)
for i in range(len(n)):
    n[i] = (n[i]/m)*100
print(sum(n)/len(n))