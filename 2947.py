def solution(lst):
    for i in range(len(lst)-1):
        a = lst[i]
        b = lst[i+1]
        if a > b:
            lst[i] = b
            lst[i+1] = a
            print(*lst)
    if lst != [1,2,3,4,5]:
        solution(lst)

lst = list(map(int,input().split()))

solution(lst)