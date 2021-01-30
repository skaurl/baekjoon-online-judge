mod = 1000000
p = mod//10*15
num = int(input())
list = [0,1]
for i in range(2,p):
    list.append((list[i-1]+list[i-2])%mod)
print(list[num%p])