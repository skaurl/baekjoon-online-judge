n = int(input())

for i in range(n):
    A = sorted(list(map(int,input().split()))[1:])
    a = []
    for j in range(1,len(A)):
        a.append(A[j]-A[j-1])
    print("Class "+str(i+1))
    print("Max "+str(max(A))+", Min "+str(min(A))+", Largest gap "+str(max(a)))