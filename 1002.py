N = int(input())
A = []
for i in range(N):
	x1, y1, r1, x2, y2, r2 = input().split()
	A.append([x1, y1, r1, x2, y2, r2])
	
for i in range(len(A)):	
	d1 = (int(A[i][0])-int(A[i][3]))**2 + (int(A[i][1])-int(A[i][4]))**2
	d2 = (int(A[i][2])+int(A[i][5]))**2
	if d1 > d2:
		print(0)
	elif d1 == d2:
		print(1)
	elif d1 < d2:
		if d1 == 0:
			if int(A[i][2])==int(A[i][5]):
				print(-1)
			else:
				print(0)
		else:
			if (int(A[i][2]) - int(A[i][5]))**2 > d1:
				print(0)
			elif (int(A[i][2]) - int(A[i][5]))**2 == d1:
				print(1)
			elif (int(A[i][2]) - int(A[i][5]))**2 < d1:
				print(2)