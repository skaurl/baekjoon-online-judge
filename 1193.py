import sys
n = int(sys.stdin.readline())
i = 0
while True:
    if i*(i+1)/2 < n and (i+1)*(i+2)/2 >= n:
        a = i+1
        break
    else:
        i+=1
b = n - a*(a-1)/2
b = int(b)
if a%2==0:
    print(b,end='')
    print('/',end='')
    print(a+1-b)
else:
    print(a+1-b,end='')
    print('/',end='')
    print(b)