n = input()
for i in range(1,len(n)+1):
    if n == "".join([n[len(n)-j-1] for j in range(len(n))]):
        print(len(n))
        break
    a = n+"".join([n[:i][len(n[:i])-j-1] for j in range(len(n[:i]))])
    b = "".join([a[len(a)-j-1] for j in range(len(a))])
    if a==b:
        print(len(a))
        break