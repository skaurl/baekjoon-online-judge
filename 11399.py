n = int(input())
lst = sorted(list(map(int,input().split())))
print(sum([(len(lst)-i)*lst[i] for i in range(len(lst))]))