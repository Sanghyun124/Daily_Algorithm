n=int(input())
k=int(input())
nums=[]
for _ in range(n):
    nums.append(input())
res=[]
def dfs(t,r,visited):
    if t==k:
        if r not in res:
            res.append(r)
        return

    for a in range(n):
        temp=r
        if not visited[a]:
            visited[a]=1
            r+=nums[a]
            dfs(t+1,r,visited)
            visited[a]=0
            r=temp
dfs(0,'',[0]*n)
print(len(res))