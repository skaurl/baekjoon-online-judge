import sys

num = int(sys.stdin.readline().strip())

lst = [0,1,1,1]

if num <= 3:
    print(lst[num])
else:
    for _ in range(num-3):
        lst.append(lst[-1]+lst[-3])
    print(lst[num])