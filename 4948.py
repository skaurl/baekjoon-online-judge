def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

while True:
    m = int(input())
    if m == 0:
        break
    n = 2*m
    l = prime_list(n+1)
    a = [l[i] for i in range(len(l)) if l[i] > m]
    print(len(a))