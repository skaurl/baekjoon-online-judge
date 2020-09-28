import sys
n = int(sys.stdin.readline())
N = []
def hanoi(n, from_pos=1, to_pos=3, aux_pos=2):
    if n == 1:
        N.append([from_pos, to_pos])
        return
    hanoi(n - 1, from_pos, aux_pos, to_pos)
    N.append([from_pos, to_pos])
    hanoi(n - 1, aux_pos, to_pos, from_pos)
hanoi(n)
print(len(N))
for i in range(len(N)):
    print(N[i][0],N[i][1])