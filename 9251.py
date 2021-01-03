a = input()
b = input()
a_len = len(a)+1
b_len = len(b)+1
lcs = [[0] * b_len for _ in range(a_len)]
for i in range(1, a_len):
    for j in range(1, b_len):
        if a[i-1] == b[j-1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
print(lcs[-1][-1])