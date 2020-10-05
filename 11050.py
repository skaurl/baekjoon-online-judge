import sys

def f(x):
    result = 1
    for i in range(x):
        result *= i+1
    return result

n = sys.stdin.readline().split()

print(int(f(int(n[0]))/(f(int(n[1]))*f(int(n[0])-int(n[1])))))