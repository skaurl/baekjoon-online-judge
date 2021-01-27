import sys

a,b = map(int,sys.stdin.readline().strip().split())

cnt = 0

lst = [True]*(a+1)
for i in range(2,a+2):
    for j in range(i,a+1,i):
        if lst[j] == True:
            lst[j] = False
            cnt += 1
            if cnt == b:
                print(j)
                break