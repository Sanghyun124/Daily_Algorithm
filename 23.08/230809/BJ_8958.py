t=int(input())
for _ in range(t):
    s=list(input())
    cnt=0
    score=0
    for x in s:
        if x=='O':
            cnt+=1
            score+=cnt
        else:
            cnt=0

    print(score)