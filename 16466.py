N = int(input())
a = input()
A = a.split(' ')
for i in range(len(A)):
	A[i] = int(A[i])
A.sort()
for i in range(N+1):
	if i == N:
		print(i+1)
	elif i+1 != A[i]:
		print(i+1)
		break
	elif i+1 == A[i]:
		continue