import sys

print(int(str(bin(int(sys.stdin.readline().strip())))[2:][::-1],2))