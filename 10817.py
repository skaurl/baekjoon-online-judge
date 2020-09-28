a = input().split()
A = int(a[0])
B = int(a[1])
C = int(a[2])
if A >= B and B >= C:
    print(B)
elif A >= C and C >= B:
    print(C)
elif B >= A and A >= C:
    print(A)
elif B >= C and C >= A:
    print(C)
elif C >= A and A >= B:
    print(A)
elif C >= B and B >= A:
    print(B)