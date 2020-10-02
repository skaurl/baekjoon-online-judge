import sys
n = list(sys.stdin.readline())[:-1]
A = [0]*11
for i in range(len(n)):
    A[int(n[i])]+=1
for i in range(len(A)):
    if A[len(A)-i-1] != 0:
        for j in range(A[len(A)-i-1]):
            print(len(A)-i-1, end='')