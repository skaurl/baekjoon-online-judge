A = [1,1,2,2,2,8]
B = list(map(int,input().split()))
C = []
for i in range(len(A)):
    C.append(str(A[i]-B[i]))
print(" ".join(C))