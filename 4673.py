def d(x):
    result = x
    for i in str(x):
        result += int(i)
    A.remove(result)
    return result

A = list(range(1,10000,1))

for i in range(1,10000,1):
    try:
        d(i)
    except:
        True

for i in A:
    print(i)