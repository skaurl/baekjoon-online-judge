import sys
n = sys.stdin.readline().split()
for i in range(len(n)):
    m = ''
    for j in range(len(n[i])):
        m += n[i][len([i])+1-j]
    m = int(m)
    n[i] = m
if n[0] > n[1]:
    print(n[0])
else:
    print(n[1])