import sys

num = int(sys.stdin.readline().strip())
lst = sorted(set(map(int, sys.stdin.readline().strip().split())))

print(*lst)