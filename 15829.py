import sys
n = int(sys.stdin.readline().strip())
N = list(sys.stdin.readline().strip())
ans = 0
for i in range(len(N)):
    ans += ((ord(N[i])-96)*(31**i))
print(ans%1234567891)