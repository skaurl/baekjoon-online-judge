n = int(input())
lst = [1,1]
for i in range(88):
    lst.append(lst[i]+lst[i+1])
print(lst[n-1])