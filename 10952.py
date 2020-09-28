A = []
while True:
    a = input()
    if a != '0 0':
        a = a.split()
        A.append(a)
    else:
        break
    
for i in range(len(A)):
    print(int(A[i][0])+int(A[i][1]))