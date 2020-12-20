A = []
for i in range(5):
    a,b,c,d = map(int, input().split())
    A.append(a+b+c+d)
print(A.index(max(A))+1,end=" ")
print(max(A))