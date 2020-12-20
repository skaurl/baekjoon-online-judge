A = []
for i in range(5):
    A.append(input())
b = ""
c = [len(i) for i in A]
c = max(c)
for i in range(c):
    for j in range(5):
        try:
            b += A[j][i]
        except:
            True
print(b)