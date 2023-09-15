n=int(input())
m=int(input())
broken=list(map(int,input().split()))

ans=abs(100-n)


for num in range(1000001):
    for x in str(num):
        if int(x) in broken:
            break
    else:
        ans=min(ans,len(str(num))+abs(num-n))

print(ans)
