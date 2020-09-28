N = int(input())
X = []
for i in range(N):
    X.append(' ')
for i in range(len(X)):
    x = ''
    X[N-1-i] = '*'
    for j in range(len(X)):
        x += X[j]
    print(x)