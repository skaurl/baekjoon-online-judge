n,m=map(int,input().split())
A = []
cnt=1
while True:
    if len(A)>=m:
        break
    A+=[cnt]*cnt
    cnt+=1
print(sum(A[n-1:m]))