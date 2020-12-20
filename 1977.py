a = int(input())
b = int(input())
c = [i**2 for i in range(1,101)]
d = []
for i in c:
    if a<=i and i<=b:
        d.append(i)
if len(d)==0:
    print(-1)
else:
    print(sum(d))
    print(min(d))