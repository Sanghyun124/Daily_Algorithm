T=int(input())
for t in range(T):
    n,m=map(int,input().split())
    num_list=list(map(int,input().split()))
    
    max_num=0
    min_num=0
    for i in range(n-m+1):
        num=0
        for j in range(m):
            num+=num_list[i+j]
        if min_num==0:
            min_num=num
        elif min_num>num:
            min_num=num
        if max_num<num:
            max_num=num
        
        
    print(f'#{t+1} {max_num-min_num}')
