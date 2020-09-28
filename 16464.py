N = int(input())
K = []
for i in range(N):
	k = int(input())
	K.append(k)
A = []
for i in range(1,30):
	A.append(2**i)

for i in range(len(K)):
	b = False
	for j in range(len(A)):
		if K[i] == A[j]:
			print('GoHanGang')
			b = True
	if b == False:
		print('Gazua')