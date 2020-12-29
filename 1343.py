n = input()
n = n.replace("XXXX","AAAA")
n = n.replace("XX","BB")
if n.find("X") == -1:
    print(n)
else:
    print(-1)