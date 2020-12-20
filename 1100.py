A = []
count = 0
for i in range(8):
    A.append(list(input()))
for i in range(8):
    for j in range(8):
        if (i+j)%2==0 and A[i][j]=="F":
            count+=1
print(count)