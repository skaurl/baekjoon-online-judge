a = int(input())
b = []
for i in range(a):
    c = int(input())
    if c == 0:
        try:
            b.pop()
        except:
            True
    else:
        b.append(c)
print(sum(b))