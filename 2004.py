import sys

def f(x,y):
    count = 0
    div = y
    while x>=div:
        count += x//div
        div *= y
    return count

n = list(map(int,sys.stdin.readline().split()))

print(min(f(n[0],2) - f(n[1],2) - f(n[0]-n[1],2) , f(n[0],5) - f(n[1],5) - f(n[0]-n[1],5)))
