T = int(input())
A = []
for i in range(T):
    a = input()
    a = a.split(' ')
    A.append(a)
for i in range(len(A)):
    b = i+1
    c = int(A[i][0])
    d = int(A[i][1])
    e = int(A[i][0])+int(A[i][1])
    print('Case #%d: %d + %d = %d'%(b, c, d, e))