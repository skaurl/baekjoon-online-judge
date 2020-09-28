import sys
n = int(sys.stdin.readline())
i = 0
while True:
    if n == 1:
        print(1)
        break
    elif (3*(i**2) +3*i +1) < n and (3*((i+1)**2) +3*(i+1) +1) >= n:
        print(i+2)
        break
    else:
        i += 1