import sys
n = int(sys.stdin.readline())
N = []
for i in range(n):
    m = input()
    N.append(m)
num = 0
for i in range(len(N)):
    l = True
    for j in range(len(list(set(list(N[i]))))):
        k = N[i][ N[i].find(list(set(list(N[i])))[j]): N[i].rfind(list(set(list(N[i])))[j])+1 ]
        if len(list(set(list(k)))) == 1:
            l = True
        else:
            l = False
            break
    if l == True:
        num += 1
print(num)