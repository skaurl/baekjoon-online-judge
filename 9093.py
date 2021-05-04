import sys

num = int(sys.stdin.readline())

for _ in range(num):
    tmp = sys.stdin.readline().split()
    ans = []
    for i in tmp:
        ans.append(i[::-1])
    print(' '.join(ans))