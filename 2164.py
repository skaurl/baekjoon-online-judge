n = int(input())

N = [1]
i = 1

while True:
    N.extend(list(range(2,2**i+1,2)))
    i+=1
    if n<=len(N):
        break

print(N[n-1])