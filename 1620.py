import sys

a,b = map(int,sys.stdin.readline().strip().split())
dict_1 = {}
dict_2 = {}

for i in range(a):
    name = sys.stdin.readline().strip()
    dict_1[name] = i+1
    dict_2[i+1] = name

for i in range(b):
    x = sys.stdin.readline().strip()
    try:
        print(dict_2[int(x)])
    except:
        print(dict_1[x])