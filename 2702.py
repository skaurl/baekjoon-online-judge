import sys

def gcd(x, y):
   while y:
       x, y = y, x % y
   return x

def lcm(x, y):
   return x * y // gcd(x,y)

num = int(sys.stdin.readline())

for _ in range(num):
    a,b = map(int,sys.stdin.readline().split())
    print(lcm(a,b),gcd(a,b))