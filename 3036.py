import sys

def printFraction(bunsu):
  print("%d/%d" % (bunsu[0], bunsu[1]))

def gcd(a, b):
  while (b != 0):
    temp = a % b
    a = b
    b = temp
  return abs(a)

def reduceFraction(bunja, bunmo):
  frac = [ bunja, bunmo ]
  if (frac[1] == 0):
    frac[0] = 0
    frac[1] = 0
    return frac
  gcd_result = gcd(frac[0], frac[1])
  frac[0] = frac[0] / gcd_result
  frac[1] = frac[1] / gcd_result
  return frac

n = int(sys.stdin.readline())
N = list(map(int, sys.stdin.readline().split()))
M = []

for i in range(len(N)-1):
    printFraction(reduceFraction(N[0], N[i+1]))