import sys
while True:
    n = sys.stdin.readline().split()
    if n == []:
        break
    else:
        print(int(n[0])+int(n[1]))