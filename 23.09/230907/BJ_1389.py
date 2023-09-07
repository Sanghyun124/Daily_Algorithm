import sys
from collections import deque

input=sys.stdin.readline

def bfs(start,end):
    q=deque([start])
    cnt=1
    while q:
        for _ in range(len(q)):
            now=q.popleft()
            if now==end:
                return cnt
            for a in p[now]:
                q.append(a)
        else:
            cnt+=1


n,m=map(int,input().split())
p=[[] for _ in range(n+1)]
res=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    p[a].append(b)
    p[b].append(a)
    res[a][b]=1
    res[b][a]=1

for x in range(n+1):
    for y in range(n+1):
        if x!=y and x!=0 and y!=0 and not res[x][y]:
            r=bfs(x,y)
            # print(r)
            res[x][y]=res[y][x]=r

min_num=10000000000000000000000
ans=0
for i in range(1,len(res)):
    if sum(res[i])<min_num:
        ans=i
        min_num=sum(res[i])

print(ans)
