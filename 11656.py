n = input()
N = []
for i in range(len(n)):
    N.append(n[i:])
N = sorted(N)
for i in N:
    print(i)