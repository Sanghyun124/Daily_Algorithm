T=int(input())
for t in range(T):
    total,submited=map(int,input().split())
    assignment=[0]*total
    student=list(map(int,input().split()))
    for i in student:
        assignment[i-1]=1
    print(f'#{t+1}',end=' ')
    for j in range(total):
        if assignment[j]==0:
            print(f'{j+1}',end=' ')
    print()
