import sys

x,y = map(str,sys.stdin.readline().strip().split())

ans = str(int(x[::-1])+int(y[::-1]))

print(int(ans[::-1]))