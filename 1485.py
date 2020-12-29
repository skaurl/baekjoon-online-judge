from collections import Counter

n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))
    ab = ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
    ac = ((a[0]-c[0])**2+(a[1]-c[1])**2)**0.5
    ad = ((a[0]-d[0])**2+(a[1]-d[1])**2)**0.5
    bc = ((b[0]-c[0])**2+(b[1]-c[1])**2)**0.5
    bd = ((b[0]-d[0])**2+(b[1]-d[1])**2)**0.5
    cd = ((c[0]-d[0])**2+(c[1]-d[1])**2)**0.5
    X = [ab,ac,ad,bc,bd,cd]
    X = sorted(list(dict(Counter(X)).values()))
    if X == [2,4]:
        print(1)
    else:
        print(0)