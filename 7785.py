n = int(input())

A = {}

for i in range(n):
    a = list(map(str,input().split()))
    if a[1] == "enter":
        A[a[0]] = 1
    elif a[1] == "leave":
        A[a[0]] = 0

A = sorted(A.items(), key= lambda x : x[0], reverse = True)

for i,j in A:
    if j == 1:
        print(i)
