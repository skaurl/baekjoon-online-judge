import sys
n = int(sys.stdin.readline())

N = list(range(1,n+1,1))
M = list(range(1,n+1,1))

for i in N:
    if i >= 100:
        if int(str(i)[0])-int(str(i)[1]) == int(str(i)[1])-int(str(i)[2]):
            True
        else:
            M.remove(i)
    else:
        True

print(len(M))