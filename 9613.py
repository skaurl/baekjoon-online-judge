from itertools import combinations

def gcd(x,y):
    while y:
        x, y = y, x%y
    return x

n = int(input())

for i in range(n):
    result = 0
    a = list(map(int,input().split()))[1:]
    for j in list(combinations(a,2)):
        b = gcd(j[0],j[1])
        result += b
    print(result)