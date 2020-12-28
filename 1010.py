def asdf(n):
    result = 1
    for i in range(1,n+1):
        result*=i
    return result

n = int(input())

for i in range(n):
    a,b=map(int,input().split())
    if a>=b:
        print(asdf(a)//(asdf(a-b)*asdf(b)))
    else:
        print(asdf(b)//(asdf(b-a)*asdf(a)))