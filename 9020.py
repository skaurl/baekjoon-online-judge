import sys

def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

def sosu(n):
    li = prime_list(n)
    idx = max([i for i in range(len(li)) if li[i]<=n/2])
    for i in range(idx,-1,-1):
        for j in range(i, len(li)):
            if li[i]+li[j]==n:
                return [li[i],li[j]]

m = int(sys.stdin.readline())
for _ in range(m):
    a = sosu(int(sys.stdin.readline()))
    print(a[0],a[1])