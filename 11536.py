import sys

num = int(sys.stdin.readline().strip())

lst = []

for _ in range(num):
    lst.append(sys.stdin.readline().strip())

lst_INCREASING = sorted(lst)
lst_DECREASING = sorted(lst, reverse=True)

if lst == lst_INCREASING:
    print('INCREASING')
elif lst == lst_DECREASING:
    print('DECREASING')
else:
    print('NEITHER')