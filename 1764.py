a,b = map(int,input().split())
A = []
B = []
for i in range(a):
    A.append(input())
for i in range(b):
    B.append(input())
A = set(A)
B = set(B)
C = sorted(A & B)
print(len(C))
for i in C:
    print(i)