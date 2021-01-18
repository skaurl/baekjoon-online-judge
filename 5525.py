import sys
a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
B = sys.stdin.readline().strip()

ans = 0
p = 0
i = 1

while i < b-1:
    if B[i-1]=="I" and B[i]=="O" and B[i+1]=="I":
        p+=1
        if p == a:
            p-=1
            ans+=1
        i+=1
    else:
        p = 0
    i += 1
print(ans)