n = int(input())
M = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14]]
for i in range(14):
    m = []
    for j in range(14):
        m.append(sum(M[i][:j+1]))
    M.append(m)
for i in range(n):
    a = int(input())
    b = int(input())
    print(M[a][b-1])