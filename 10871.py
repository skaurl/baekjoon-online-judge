import sys
n1 = sys.stdin.readline().split()
n2 = sys.stdin.readline().split()
for i in range(int(n1[0])):
    if int(n2[i]) < int(n1[1]):
        print(n2[i],end=' ')