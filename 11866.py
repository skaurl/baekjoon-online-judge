n,m = map(int,input().split())
a = list(range(1,n+1))
b = list(range(1,n+1))
ans = []
cnt = 1
while True:
    if len(ans) == n:
        break
    try:
        ans.append(a[m*cnt-1])
        b.remove(a[m*cnt-1])
        cnt+=1
    except:
        a+=b
ans = [str(i) for i in ans]
print("<"+", ".join(ans)+">")