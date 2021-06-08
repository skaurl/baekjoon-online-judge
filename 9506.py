while True:
    n = int(input())
    if n==-1:
        break
    temp_n=[]
    for i in range(1,n+1):
        if n%i==0:
            temp_n.append(i)
    sum_l=0
    sum_r=temp_n[len(temp_n)-1]
    for i in temp_n[:-1]:
        sum_l+=i
    if sum_l==sum_r:
        answer=str(sum_r)+" = "+str(temp_n[0])
        for i in range(1,len(temp_n)-1):
            answer+=" + "+str(temp_n[i])
        print(answer)
    else:
        print(str(temp_n[-1])+" is NOT perfect.")