from itertools import combinations

a,b = map(int,input().split())
lst = list(map(int,input().split()))
cnt = 0
for i in range(1,a+1,1):
    c = list(combinations(lst,i))
    for j in c:
        if sum(j) == b:
            cnt +=1
print(cnt)