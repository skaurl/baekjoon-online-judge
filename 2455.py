A = []
for i in range(4):
    m,n = map(int, input().split())
    A.append(n-m)
for i in range(3):
    A[i+1] = A[i] + A[i+1]
print(max(A))