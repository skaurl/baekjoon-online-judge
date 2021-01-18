import sys
num = int(sys.stdin.readline().strip())
lst_1 = list(map(int,sys.stdin.readline().strip().split()))
lst_2 = list(sorted(set(lst_1)))
lst_2 = {lst_2[i]:i for i in range(len(lst_2))}
print(*[lst_2[i] for i in lst_1])