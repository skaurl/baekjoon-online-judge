a,b = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
C = sorted(A-B)
C = [str(i) for i in C]
print(len(C))
print(" ".join(C))