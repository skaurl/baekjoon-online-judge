import sys

num = int(sys.stdin.readline().strip())

lst = [0,1]

for i in range(2,abs(num)+1):
    lst.append((lst[i-1]+lst[i-2])%1000000000)
if num%2==0 and num<0:
    print(-1)
elif num==0:
    print(0)
else:
    print(1)

print(lst[abs(num)])