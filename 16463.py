N = int(input())
A = []
for i in range(2019,N+1,1):
	if i%4 == 0:
		if i%400 == 0:
			A.extend([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
		elif i%100 == 0:
			A.extend([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
		else:
			A.extend([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
	else:
		A.extend([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
B = []
for i in range(len(A)):
	B.append(A[i]%7)
C = ['월','화','수','목','금','토','일']
D = [1]
for i in range(len(B)-1):
	D.append((D[i]+B[i])%7)
count = 0
for i in range(len(D)):
	if D[i] == 6:
		count += 1
print(count)