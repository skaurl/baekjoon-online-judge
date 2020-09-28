N = int(input())
X = []
for i in range(N):
    X.append('*')
for i in range(len(X)):
    x = ''
    for j in range(len(X)):
        x += X[j]
    print(x)
    X[i] = ' '