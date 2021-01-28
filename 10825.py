import sys
num = int(sys.stdin.readline().strip())
lst = []
for i in range(num):
    a,b,c,d = map(str,sys.stdin.readline().strip().split())
    tmp = [a,int(b),int(c),int(d)]
    lst.append(tmp)
lst = sorted(lst, key = lambda x : (-x[1], x[2], -x[3], x[0]))
for i in lst:
    print(i[0])