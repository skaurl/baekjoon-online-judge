import math

def primeSieve(sieveSize):
    sieve = [True] * (sieveSize+1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2,int(math.sqrt(sieveSize))+1):
        if sieve[i] == False:
            continue
        for pointer in range(i**2, sieveSize+1, i):
            sieve[pointer] = False
    primes = []
    for i in range(sieveSize+1):
        if sieve[i] == True:
            primes.append(i)
    return primes

def get_prime_factors(n):
    primelist = primeSieve(n)
    factors = []
    for p in primelist:
        count = 0
        while n % p == 0:
            n /= p
            count += 1
        if count > 0:
            factors.append((p, count))
    return factors
n = int(input())

for i in range(n):
    A = get_prime_factors(int(input()))
    for i,j in A:
        print(i,j)