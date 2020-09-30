import sys
a = int(sys.stdin.readline())
b = []

for i in range(1,a+1,1):
    result = i + (i//1)%10 + (i//10)%10 + (i//100)%10 + (i//1000)%10 + (i//10000)%10 + (i//100000)%10 + (i//1000000)%10
    if result == a:
        b.append(i)

if len(b) == 0:
    print(0)
else:
    print(min(b))