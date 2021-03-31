import sys

num = int(sys.stdin.readline().strip())

for _ in range(num):
    s,e = map(int,sys.stdin.readline().strip().split())
    cnt = 0
    for num in range(s,e+1):
        cnt += str(num).count('0')
    print(cnt)