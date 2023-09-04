n,m=map(int,input().split())

nums=list(map(int,input().split()))

res=0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            temp=nums[i]+nums[j]+nums[k]
            if temp<=m and m-temp<m-res:
                res=temp

print(res)