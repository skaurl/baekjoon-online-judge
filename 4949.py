while True:
    n = input()
    if n == ".":
        break
    stack = [""]
    for i in range(len(n)):
        if n[i]=="(":
            stack.append(n[i])
        elif n[i]=="[":
            stack.append(n[i])
        elif n[i]==")":
            stack.append(n[i])
            if stack[-2]+stack[-1] == "()":
                stack.pop()
                stack.pop()
        elif n[i]=="]":
            stack.append(n[i])
            if stack[-2]+stack[-1] == "[]":
                stack.pop()
                stack.pop()
    stack = stack[1:]
    if len(stack) == 0:
        print("yes")
    else:
        print("no")