import sys
n = list(sys.stdin.readline())
del n[-1]
m = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
M = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(len(n)):
    if n[i] == 'a' or n[i] == 'A':
        m[0] += 1
    elif n[i] == 'b' or n[i] == 'B':
        m[1] += 1
    elif n[i] == 'c' or n[i] == 'C':
        m[2] += 1
    elif n[i] == 'd' or n[i] == 'D':
        m[3] += 1
    elif n[i] == 'e' or n[i] == 'E':
        m[4] += 1
    elif n[i] == 'f' or n[i] == 'F':
        m[5] += 1
    elif n[i] == 'g' or n[i] == 'G':
        m[6] += 1
    elif n[i] == 'h' or n[i] == 'H':
        m[7] += 1
    elif n[i] == 'i' or n[i] == 'I':
        m[8] += 1
    elif n[i] == 'j' or n[i] == 'J':
        m[9] += 1
    elif n[i] == 'k' or n[i] == 'K':
        m[10] += 1
    elif n[i] == 'l' or n[i] == 'L':
        m[11] += 1
    elif n[i] == 'm' or n[i] == 'M':
        m[12] += 1
    elif n[i] == 'n' or n[i] == 'N':
        m[13] += 1
    elif n[i] == 'o' or n[i] == 'O':
        m[14] += 1
    elif n[i] == 'p' or n[i] == 'P':
        m[15] += 1
    elif n[i] == 'q' or n[i] == 'Q':
        m[16] += 1
    elif n[i] == 'r' or n[i] == 'R':
        m[17] += 1
    elif n[i] == 's' or n[i] == 'S':
        m[18] += 1
    elif n[i] == 't' or n[i] == 'T':
        m[19] += 1
    elif n[i] == 'u' or n[i] == 'U':
        m[20] += 1
    elif n[i] == 'v' or n[i] == 'V':
        m[21] += 1
    elif n[i] == 'w' or n[i] == 'W':
        m[22] += 1
    elif n[i] == 'x' or n[i] == 'X':
        m[23] += 1
    elif n[i] == 'y' or n[i] == 'Y':
        m[24] += 1
    elif n[i] == 'z' or n[i] == 'Z':
        m[25] += 1
z = 0
for i in range(len(m)):
    if m[i] == max(m):
        z += 1
if z != 1:
    print('?')
else:
    for i in range(len(m)):
        if m[i] == max(m):
            print(M[i])