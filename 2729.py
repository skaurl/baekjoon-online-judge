import sys

num = int(sys.stdin.readline().strip())

for _ in range(num):
    tmp = [int(i,2) for i in sys.stdin.readline().strip().split()]
    print(bin(sum(tmp))[2:])