import sys

n = int(sys.stdin.readline().strip())

lst = [1,1]

for i in range(n-1):
    lst.append(lst[i]+lst[i+1])

print(lst[n]%10007)