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

prime = primeSieve(8000000)

print(prime[int(input())-1])