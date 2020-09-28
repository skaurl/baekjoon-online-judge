import math

a = int(input())
arr = [[' ' for i in range(2187)] for j in range(2187)]

def star(a, x, y):
    if a == 3:
        arr[x][y] = '*'
        arr[x + 1][y] = '*'
        arr[x + 2][y] = '*'
        arr[x][y + 1] = '*'
        arr[x + 2][y + 1] = '*'
        arr[x][y + 2] = '*'
        arr[x + 1][y + 2] = '*'
        arr[x + 2][y + 2] = '*'
    else:
        div = math.floor(a / 3)
        star(div, x, y)
        star(div, x + div, y)
        star(div, x + 2 * div, y)
        star(div, x, y + div)
        star(div, x + 2 * div, y + div)
        star(div, x, y + 2 * div)
        star(div, x + div, y + 2 * div)
        star(div, x + 2 * div, y + 2 * div)

star(a, 0, 0)

for i in range(a):
    for j in range(a):
        print(arr[i][j], end='')
    print()