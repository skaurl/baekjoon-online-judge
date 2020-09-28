n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    c = b - a
    d = int(c ** 0.5)
    if c == 1:
        print(1)
    elif d**2 == c:
        print(2*d-1)
    elif d**2 < c and c <= (d)**2 + d:
        print(2*d)
    elif c > (d)**2 + d and c <= (d+1)**2:
        print(2*d+1)