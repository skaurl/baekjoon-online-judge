a = input().split()
A = int(a[0])
B = int(a[1])
if B - 45 >= 0:
    print(A,B-45)
else:
    if A == 0:
        print(23,B+15)
    else:
        print(A-1,B+15)