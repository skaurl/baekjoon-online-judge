import sys

def gcd(x, y):
   while y:
       x, y = y, x % y
   return x

a,b = map(int,sys.stdin.readline().strip().split(':'))

print(str(a//gcd(a,b))+':'+str(b//gcd(a,b)))
