import sys
m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
k = []
for i in range(m,n+1,1):
    l = False
    for j in range(2,i,1):
        if i%j == 0:
            l = True
            break
    if l == False:
        k.append(i)

if m ==1 and n==1:
    print(-1)
elif m==1:
    del k[0]
    print(sum(k))
    print(min(k))
elif k != []:
    print(sum(k))
    print(min(k))
else:
    print(-1)