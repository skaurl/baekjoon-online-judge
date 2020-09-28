a = input()
a = a.split(' ')
N = int(input())
B = []
for i in range(N):
	b = input()
	b = b.split(' ')
	B.append(b)
C = []
k = False
for i in range(N):
	if a[1] == 'FM' or a[1] == 'MF' or a[1] == B[i][1]:
		if int(a[2]) >= int(B[i][2]):
			C.append(B[i][0])
			k = True
if k == False:
	print('No one yet')
C.sort()
for i in C:
	print(i)