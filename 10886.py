n = int(input())
N = []
for i in range(n):
    N.append(int(input()))
if sum(N)<=n//2:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")