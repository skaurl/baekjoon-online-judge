a,b=map(int,input().split())
q = a//b
r = a%b
ans = 1
while b>0:
    if r>0:
        ans *= (q+1)
        r -= 1
    else:
        ans *= q
    b -= 1
print(ans)