n = int(input())
for i in range(n):
    a, b, c = map(int,input().split())
    d = c % a
    e = c // a
    if d == 0:
        print(a*100+e)
    else:
        print(d*100+e+1)