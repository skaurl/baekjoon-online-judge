import sys
a = sys.stdin.readline().split()
b = sys.stdin.readline().split()
c = []
d = []

n = int(a[0])
m = int(a[1])

for i in range(0,n-2,1):
    for j in range(i+1,n-1,1):
        for k in range(j+1,n,1):
            c.append(int(b[i])+int(b[j])+int(b[k]))

for i in range(len(c)):
    if c[i] <= m:
        d.append(c[i])

print(max(d))