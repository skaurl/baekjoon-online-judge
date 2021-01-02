def factorial(n):
    result = 1
    for i in range(n):
        result *= i+1
    return result

def combination(n,m):
    m = min(m,n-m)
    result = factorial(n)//(factorial(m)*factorial(n-m))
    return result

n,m = map(int,input().split())
print(combination(n,m))