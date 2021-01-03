a = [0]+list(input().strip())
b = [0]+list(input().strip())
a_len = len(a)
b_len = len(b)
lcs = [[""] * b_len for _ in range(a_len)]
for i in range(1, a_len):
    for j in range(1, b_len):
        if a[i] == b[j]:
            lcs[i][j] = lcs[i - 1][j - 1] + a[i]
        else:
            if len(lcs[i-1][j]) >= len(lcs[i][j-1]):
                lcs[i][j] = lcs[i-1][j]
            else:
                lcs[i][j] = lcs[i][j-1]
print(len(lcs[-1][-1]))
print(lcs[-1][-1])