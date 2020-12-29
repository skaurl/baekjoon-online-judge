a,b=map(int,input().split())
A = list(range(1,a+1))
B = []
C = [i for i in A]
i = 0
while True:
    if len(B) == a:
        break
    try:
        B.append(str(A[((i+1)*(b)-1)]))
        C.remove(A[((i+1)*(b)-1)])
        i+=1
    except:
        A+=C
        try:
            B.append(str(A[((i+1)*(b)-1)]))
            C.remove(A[((i+1)*(b)-1)])
            i += 1
        except:
            pass
print("<"+", ".join(B)+">")