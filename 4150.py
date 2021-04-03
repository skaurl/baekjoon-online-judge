import sys

num = int(sys.stdin.readline().strip())

lst = [0,1,1]
for i in range(3,num+1):
    lst.append(lst[i-1]+lst[i-2])

print(lst[num])