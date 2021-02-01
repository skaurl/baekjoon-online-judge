import sys

num_1 = int(sys.stdin.readline().strip())
lst = list(map(int,sys.stdin.readline().strip().split()))
cum = [0]
for i in range(len(lst)):
    cum.append(cum[-1]+lst[i])

num_2 = int(sys.stdin.readline().strip())
for i in range(num_2):
    a,b = map(int,sys.stdin.readline().strip().split())
    print(cum[b]-cum[a-1])