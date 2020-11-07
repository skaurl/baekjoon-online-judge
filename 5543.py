import sys

n_1 = int(sys.stdin.readline())
n_2 = int(sys.stdin.readline())
n_3 = int(sys.stdin.readline())
n_4 = int(sys.stdin.readline())
n_5 = int(sys.stdin.readline())

N = []

N.append(n_1 + n_4)
N.append(n_1 + n_5)
N.append(n_2 + n_4)
N.append(n_2 + n_5)
N.append(n_3 + n_4)
N.append(n_3 + n_5)

print(min(N)-50)