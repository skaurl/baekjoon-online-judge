n = int(input())
lst = [1,1,1]
for i in range(100):
    lst.append(lst[i]+lst[i+1])
for i in range(n):
    print(lst[int(input())-1])