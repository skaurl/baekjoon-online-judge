a,b = map(int,input().split())
lst = []
for i in range(a):
    lst.append(int(input()))
dp = [0]*(b+1)
dp[0] = 1
for i in lst:
    for j in range(1,b+1):
        if j-i>=0:
            dp[j]+=dp[j-i]
print(dp[b])