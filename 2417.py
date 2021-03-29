import sys

num = int(sys.stdin.readline().strip())

print(int(num**0.5)+1 if num**0.5%1!=0 else int(num**0.5))