import sys

n = int(sys.stdin.readline().strip())

lst_1 = [1,1]
lst_2 = [1,1]

for i in range(n-1):
    lst_1.append(lst_1[i]+lst_1[i+1])
    lst_2.append(2*lst_2[i]+lst_2[i + 1])

print(lst_2[n]%10007)