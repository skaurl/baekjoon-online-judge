def asdf(n):
    result = 0
    for i in n:
        result+=int(i)
    return str(result)

n = input()
cnt = 0

if int(asdf(n))%3==0:
    check="YES"
else:
    check="NO"

while len(n)!=1:
    n = asdf(n)
    cnt+=1

print(cnt)
print(check)