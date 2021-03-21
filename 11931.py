import sys

num = int(sys.stdin.readline().strip())
lst = []
for _ in range(num):
    lst.append(int(sys.stdin.readline().strip()))

for i in sorted(lst,reverse=True):
    print(i)