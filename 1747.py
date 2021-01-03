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

def check(n):
    ch = True
    for j in range(len(str(n))):
        if str(n)[j] != str(n)[len(str(n))-j-1]:
            ch = False
            break
    if ch == True:
        return True
    else:
        return False

ans = []

for i in primeSieve(1003002):
    if check(i) == True:
        ans.append(i)

n = int(input())

for i in ans:
    if n<=i:
        print(i)
        break