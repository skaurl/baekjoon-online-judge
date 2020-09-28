import sys
n = list(sys.stdin.readline())
del n[-1]
N = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
M = ['','','','','','','','','','','','','','','','','','','','','','','','','','',]
for i in range(len(n)):
    for j in range(len(N)):
        if n[i] == N[j]:
            M[j] = i
            N[j] = j
            break
for i in range(len(M)):
    if M[i] == '':
        M[i] = -1
for i in range(len(M)):
    print(M[i],end=' ')