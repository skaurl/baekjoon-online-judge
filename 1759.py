from itertools import combinations

a,b = map(int, input().split())
lst = list(map(str,input().split()))
ans = []
for i in combinations(lst,a):
    if len(set(i)&set("aeiou"))!=0 and len(set(i)&set("bcdfghjklmnpqrstvwxyz"))>=2:
        ans.append("".join(sorted(i)))
ans=sorted(ans)
for i in ans:
    print(i)