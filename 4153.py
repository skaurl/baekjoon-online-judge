while True:
    A = input().split()
    A[0] = int(A[0])
    A[1] = int(A[1])
    A[2] = int(A[2])
    A = sorted(A)
    if A[0] == 0 and A[1] == 0 and A[2] == 0:
        break
    if A[0]**2 + A[1]**2 == A[2]**2:
        print('right')
    else:
        print('wrong')