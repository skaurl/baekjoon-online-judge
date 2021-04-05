import sys

num = int(sys.stdin.readline().strip())

lst = []

for _ in range(num):
    lst.append(list(map(int, sys.stdin.readline().strip().split())))

if num == 2:
    print(1,1)
else:
    a = (lst[0][1]+lst[0][2]-lst[1][2])//2
    ans = [a]
    for i in lst[0][1:]:
        ans.append(i-a)
    print(*ans)