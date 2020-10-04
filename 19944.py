import sys
n = sys.stdin.readline().split()

if int(n[1]) == 1 or int(n[1]) == 2:
    print('NEWBIE!')
elif int(n[0]) >= int(n[1]):
    print('OLDBIE!')
else:
    print('TLE!')