def round2(num):
    return int(num) + 1 if num - int(num) >= 0.5 else int(num)

n=int(input())
score=[int(input()) for _ in range(n)]
score.sort()
exception=round2(n*0.15)
temp=score[exception:n-exception]
print(temp)
if n:
    res=round2(sum(temp)/len(temp))
    print(res)
else:
    print(0)
