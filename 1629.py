import sys

def f(x,y,z):
    if y == 1:
        return x % z
    else:
        tmp = f(x,y//2,z)
        if y % 2 == 0:
            return (tmp**2) % z
        else:
            return ((tmp ** 2)*x) % z

num = list(map(int,sys.stdin.readline().strip().split()))

print(f(num[0],num[1],num[2]))