import sys

A,B = map(str,sys.stdin.readline().split())
A = int(A,2)
B = int(B,2)
C = A + B

print(bin(C)[2:])