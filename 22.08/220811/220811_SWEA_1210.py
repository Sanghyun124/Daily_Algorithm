for t in range(10):
    n=int(input())
    ladder=[list(map(int,input().split())) for _ in range(100)]
    for point in range(100):
        if ladder[99][point]==2:
            start=point
            break
    i=99
    j=start
    while i>0:
        i-=1
        if j<99 and ladder[i][j+1]==1:
            while j<99 and ladder[i][j+1]==1:
                j+=1
        elif j>0 and ladder[i][j-1]==1:
            while j>0 and ladder[i][j-1]==1:
                j-=1

    print(f'{t+1} {j}')
