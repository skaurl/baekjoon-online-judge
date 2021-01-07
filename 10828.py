import sys

n = int(sys.stdin.readline().strip())
stack = []
for i in range(n):
    N = sys.stdin.readline().strip()
    if N[:4] == "push":
        N = N.split()
        stack.append(int(N[1]))
    elif N == "pop":
        try:
            print(stack.pop())
        except:
            print(-1)
    elif N == "size":
        print(len(stack))
    elif N == "empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif N == "top":
        try:
            print(stack[-1])
        except:
            print(-1)