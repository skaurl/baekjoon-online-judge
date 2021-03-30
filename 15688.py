import sys

num = int(sys.stdin.readline().strip())
lst = []
for _ in range(num):
    tmp = int(sys.stdin.readline().strip())
    lst.append(tmp)

lst = sorted(lst)

for i in lst:
    print(i)