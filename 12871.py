import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

for i in range(len(s)*len(t)):
    if s[i%len(s)] != t[i%len(t)]:
        print(0)
        break
else:
    print(1)