import sys
n = list(map(int,sys.stdin.readline().split()))
m_1 = n[0]
m_2 = n[1]
n_1 = n[0]
n_2 = n[1]
N_1 = []
N_2 = []

i = 2
while n_1 != 1:
    if n_1%i==0:
        N_1.append(i)
        n_1 /= i
    else:
        i += 1

i = 2
while n_2 != 1:
    if n_2%i==0:
        N_2.append(i)
        n_2 /= i
    else:
        i += 1

A = list(set(N_1)&set(N_2))

lcm = 1

for i in range(len(A)):
    if N_1.count(A[i]) >= N_2.count(A[i]):
        lcm *= N_2.count(A[i]) * A[i]
    else:
        lcm *= N_1.count(A[i]) * A[i]

print(lcm)
print(lcm * (m_1//lcm) * (m_2//lcm))