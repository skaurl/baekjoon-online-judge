import sys

num = int(sys.stdin.readline().strip())
dp = [0]*(num+1)
square = [i**2 for i in range(1,317)]

for i in range(1, num+1):
    tmp = []
    for j in square:
        if j>i:
            break
        tmp.append(dp[i-j])
    dp[i] = min(tmp) + 1

print(dp[num])