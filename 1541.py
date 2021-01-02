n = input()
N = n.split("-")
result = []
for i in N:
    result.append(sum([int(j) for j in i.split("+")]))
for i in range(1,len(result)):
    result[0] -= result[i]
print(result[0])