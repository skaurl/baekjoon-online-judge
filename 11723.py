import sys
n = int(sys.stdin.readline().strip())
tmp = set()
for i in range(n):
    N = sys.stdin.readline().strip()
    if N[:3] == "add":
        N = N.split()
        try:
            tmp.add(int(N[1]))
        except:
            pass
    elif N[:6] == "remove":
        N = N.split()
        try:
            tmp.remove(int(N[1]))
        except:
            pass
    elif N[:5] == "check":
        N = N.split()
        if int(N[1]) in tmp:
            print(1)
        else:
            print(0)
    elif N[:6] == "toggle":
        N = N.split()
        if int(N[1]) in tmp:
            tmp.remove(int(N[1]))
        else:
            tmp.add(int(N[1]))
    elif N == "all":
        tmp = set(list(range(1,21,1)))
    elif N == "empty":
        tmp = set()