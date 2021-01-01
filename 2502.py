a,b = map(int,input().split())

lst = [(1,0),(0,1)]

for i in range(a-2):
    lst.append((lst[i][0]+lst[i+1][0],lst[i][1]+lst[i+1][1]))

x = [i[0] for i in lst][-1]
y = [i[1] for i in lst][-1]

A = []

for i in range(1,b//x+1):
    for j in range(1,b//y+1):
        z = False
        if i*x+j*y==b:
            print(i)
            print(j)
            z = True
            break
    if z==True:
        break
