N = int(input())
A = []
for i in range(N):
	a = int(input())
	A.append(a)

for i in range(len(A)):
	if A[i] == 0:
		print(1,0)
	else:
		print(int((((1+5**0.5)/2)**(A[i]-1))/(5**0.5) - (((1-5**0.5)/2)**(A[i]-1))/(5**0.5) + 0.0001), int((((1+5**0.5)/2)**(A[i]))/(5**0.5) - (((1-5**0.5)/2)**(A[i]))/(5**0.5) + 0.0001))