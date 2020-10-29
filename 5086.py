import sys

def f(n,m):
    if m % n == 0:
        return print('factor')
    elif n % m == 0:
        return print('multiple')
    else:
        return print('neither')

while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    else:
        f(n,m)