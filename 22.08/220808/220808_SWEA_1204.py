T=int(input())
for test_case in range(1, T + 1):
    t=int(input())
    score=list(map(int,input().split()))
    count_list=[0]*(max(score)+1)
    for i in score:
        count_list[i]+=1
    count_list=count_list[::-1]
    max_count=max(score)-count_list.index(max(count_list))
    print(f'#{t} {max_count}')
