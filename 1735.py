def gcd(x,y):
    while y:
        x,y=y,x%y
    return x

def lcm(x,y):
    return x*y//gcd(x,y)

a = list(map(int,input().split()))
b = list(map(int,input().split()))

A = (a[0]*(lcm(a[1],b[1])//a[1])+b[0]*(lcm(a[1],b[1])//b[1]))
B = lcm(a[1],b[1])

print(A//gcd(A,B),B//gcd(A,B))