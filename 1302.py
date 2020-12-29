n = int(input())
A = {}
for i in range(n):
    a = input()
    try:
        A[a]+=1
    except:
        A[a]=1
m = max(A.values())
B = []
for i,j in A.items():
    if j==m:
        B.append(i)
print(sorted(B)[0])