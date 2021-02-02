import sys
lst = []
for i in range(1,9):
    lst.append([int(sys.stdin.readline().strip()),i])
lst = sorted(lst,reverse=True)
print(sum([lst[i][0] for i in range(5)]))
print(*sorted([lst[i][1] for i in range(5)]))