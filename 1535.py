from itertools import combinations
n = int(input())
d = list(map(int,input().split()))
h = list(map(int,input().split()))
ans=[]
for i in range(1,n+1):
    a = list(combinations(d,i))
    a = [sum(i) for i in a]
    b = list(combinations(h,i))
    b = [sum(i) for i in b]
    for j in range(len(a)):
        if a[j]<100:
            ans.append(b[j])
try:
    print(max(ans))
except:
    print(0)