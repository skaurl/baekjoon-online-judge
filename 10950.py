T = int(input())
A = []
for i in range(T):
    a = input()
    a = a.split()
    A.append(a)
    print(int(A[i][0])+int(A[i][1]))