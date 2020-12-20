m, n = map(int, input().split())
A = [31,28,31,30,31,30,31,31,30,31,30,31]
B = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
if m==1:
    print(B[n%7])
else:
    print(B[(sum(A[:m-1])+n)%7])