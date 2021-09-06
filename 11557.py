n = int(input())
for i in range(n):
    tmp = {}
    for j in range(int(input())):
        a,b = input().split()
        b = int(b)
        try:
            tmp[a] += b
        except:
            tmp[a] = b
    print(list(tmp.keys())[list(tmp.values()).index(max(tmp.values()))])