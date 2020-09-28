import sys
n = sys.stdin.readline()
i = 0
m = int(n)
while True:
    n = str(int(n))
    if int(n) < 10:
        n = '0' + n
    a = int(n[0]) + int(n[1])
    a = str(a)
    if len(a) == 1:
        n = n[1] + a[0]
    else:
        n = n[1] + a[1]
    i = i + 1
    if int(n) == m:
        break
print(i)