n = list(input())
ans = 0
stack = []
for i in range(len(n)):
    if n[i] == "(":
        stack.append(n[i])
    elif n[i] == ")":
        if n[i-1] == "(":
            stack.pop()
            ans+=len(stack)
        else:
            stack.pop()
            ans+=1
print(ans)