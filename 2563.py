import sys

num = int(sys.stdin.readline())

paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(num):
    x,y = map(int,sys.stdin.readline().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            paper[i][j] = 1

answer = 0

for i in paper:
    answer += i.count(1)

print(answer)