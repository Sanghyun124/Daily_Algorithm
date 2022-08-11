T=int(input())
for t in range(T):
    n=int(input())
    num_list=list(map(int,list(input())))
    count_ary=[0]*10
    max_num=0
    max_index=0
    for i in num_list:
        count_ary[i]+=1 
        if max_num==count_ary[i] and max_index<i:
            max_index=i
            max_num=count_ary[i]
        elif max_num<count_ary[i]:
            max_index=i
            max_num=count_ary[i]
            
    print(f'#{t+1} {max_index} {count_ary[max_index]}')
    
