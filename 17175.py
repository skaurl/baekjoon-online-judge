import sys

num = int(sys.stdin.readline().strip())

if num < 2:
    print(1)
else:
    a,b = 1,1
    for i in range(num-1):
        a,b = a+b+1,a
    print(a%1000000007)