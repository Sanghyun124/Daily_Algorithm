T=int(input())
for t in range(T):
    n=int(input())
    ary=list(map(int,input().split()))
    
    for i in range(n-1,0,-1):
        for j in range(i):
            if ary[j]>ary[j+1]:
                ary[j],ary[j+1]=ary[j+1],ary[j]
    
    print(f'#{t+1}',end=' ')
    for k in range(n):
        print(ary[k],end=' ')
    print()
            
