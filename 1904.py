n = int(input())
dp = [1,2] + [0]*999998
for i in range(2,len(dp)):
    dp[i] = (dp[i-2]+dp[i-1])%15746
print(dp[n-1])