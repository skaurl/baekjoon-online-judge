import sys

num = int(sys.stdin.readline().strip())

for i in range(num):
    lst = sorted(map(int,sys.stdin.readline().strip().split()))
    print(lst[-3])