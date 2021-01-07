import sys

def asdf(n):
    n_1 = str(n)
    n_2 = "".join([n_1[len(n_1)-1-i] for i in range(len(n_1))])
    if n_1 == n_2:
        return "yes"
    else:
        return "no"

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    else:
        print(asdf(n))