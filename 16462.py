N = int(input())
Q = []
for i in range(N):
	q = int(input())
	Q.append(q)
for i in range(len(Q)):
	if Q[i] == 99 or Q[i] == 96 or Q[i] == 90:
		Q[i] = 99
	elif Q[i] == 89 or Q[i] == 86 or Q[i] == 80:
		Q[i] = 89
	elif Q[i] == 79 or Q[i] == 76 or Q[i] == 70:
		Q[i] = 79
	elif Q[i] == 69 or Q[i] == 66 or Q[i] == 60:
		Q[i] = 99
	elif Q[i] == 61:
		Q[i] = 91
	elif Q[i] == 62:
		Q[i] = 92
	elif Q[i] == 63:
		Q[i] = 93
	elif Q[i] == 64:
		Q[i] = 94
	elif Q[i] == 65:
		Q[i] = 95
	elif Q[i] == 67:
		Q[i] = 97
	elif Q[i] == 68:
		Q[i] = 98
	elif Q[i] == 59 or Q[i] == 56 or Q[i] == 50:
		Q[i] = 59
	elif Q[i] == 49 or Q[i] == 46 or Q[i] == 40:
		Q[i] = 49
	elif Q[i] == 39 or Q[i] == 36 or Q[i] == 30:
		Q[i] = 39
	elif Q[i] == 29 or Q[i] == 26 or Q[i] == 20:
		Q[i] = 29
	elif Q[i] == 19 or Q[i] == 16 or Q[i] == 10:
		Q[i] = 19
	elif Q[i] == 9 or Q[i] == 6 or Q[i] == 0:
		Q[i] = 9
P = []
R = {}
for i in range(len(Q)):
	P.append(Q[i])
sum = 0
for i in range(len(P)):
	sum += P[i]
avg = sum / N
if (avg-int(avg)) >= 0.5:
	print(int(avg)+1)
else:
	print(int(avg))