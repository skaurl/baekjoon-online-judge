import sys
d = [0, 1, 2, 4]
for i in range(4, 1000001):
    d.append((d[i-1]+d[i-2]+d[i-3])%1000000009)
for _ in range(int(sys.stdin.readline())):
    print(d[int(sys.stdin.readline())])