def gcd(x,y):
    while y:
        x,y=y,x%y
    return x

g,l = map(int,input().split())
q = l//g

a,b = 1,q

for i in range(1,q//2+1):
    if q%i==0:
        c = i
        d = q//i
        if gcd(c,d)!=1:
            continue
        if a+b > c+d:
            a=c
            b=d

print(a*g,b*g)