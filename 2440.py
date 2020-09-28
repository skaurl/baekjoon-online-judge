N = int(input())
x = ''
for i in range(N):
    x += '*'
for i in range(N):
    print(x)
    x = x[1:]