T=int(input())
for t in range(T):
    n,m=map(int,input().split())
    ary=[list(map(int,input().split())) for _ in range(n)]
     
    max_num=0
     
    for i in range(n-m+1):
        for j in range(n-m+1):
            total=0
            for a in range(m):
                for b in range(m):
                    total+=ary[i+a][j+b]
                    max_num=total if total>max_num else max_num
    print(f'#{t+1} {max_num}')
