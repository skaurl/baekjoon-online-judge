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

a,b=map(int,input().split())
lst=[]
c = primeSieve(10**7)
for i in range(len(c)):
    cnt = 2
    while True:
        if c[i]**cnt>=a and c[i]**cnt<=b:
            lst.append(c[i]**cnt)
        elif c[i]**cnt>b:
            break
        cnt += 1
print(len(lst))