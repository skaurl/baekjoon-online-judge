import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
N_lst = list(map(int,sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
M_lst = list(map(int,sys.stdin.readline().strip().split()))
N_lst_cnt = Counter(N_lst)
for i in range(M):
    print(N_lst_cnt[M_lst[i]],end=" ")