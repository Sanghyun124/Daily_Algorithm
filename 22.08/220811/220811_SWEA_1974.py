def is_correct(ary):
    count=0
    for i in range(9):
        count+=(1 if ary[i]==1 else 0)
    return count


T=int(input())
for t in range(T):
    sudoku=[list(map(int,input().split())) for _ in range(9)]
    a=0
    b=0
    c=0
    
    for i in range(9):
        check=[0 for _ in range(9)]
        for j in range(9):
            check[sudoku[i][j]-1]=1
        if is_correct(check)!=9:
            a=1
            
    for j in range(9):
        check=[0 for _ in range(9)]
        for i in range(9):
            check[sudoku[i][j]-1]=1
        if is_correct(check)!=9:
            b = 1
    
    for i in range(3):
        for j in range(3):
            check=[0 for _ in range(9)]
            for x in range(3):
                for y in range(3):
                    check[sudoku[(3*i)+x][(3*j)+y]-1]=1
            if is_correct(check)!=9:
                c=1
                
    print(f'#{t+1} ',end='')
    if a + b + c>0:
        print(0)
    else:
        print(1)

