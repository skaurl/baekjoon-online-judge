def gcd(x,y):
    while y:
        x,y=y,x%y
    return x

a,b = map(int,input().split())
print("1"*gcd(a,b))