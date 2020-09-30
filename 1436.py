import sys
a = int(sys.stdin.readline())

A = []
i = 0

while len(A) != 10000:
    i += 1
    if str(i).count('666') >= 1:
        A.append(i)

print(A[a-1])