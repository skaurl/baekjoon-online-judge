m = list(input())
n = []
for i in range(10):
    n.append(m.count(str(i)))

n[6] = n[6] + n[9]

if n[6]%2==0:
    n[6] = n[6]//2
else:
    n[6] = n[6] // 2 + 1

del n[9]

print(max(n))