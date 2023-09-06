import sys
from collections import deque

input=sys.stdin.readline

di=[1,0,-1,0]
dj=[0,1,0,-1]

n,m=map(int,input().split())
ary=[list(map(int,input().split())) for _ in range(n)]

start=[]

for i in range(n):
    for j in range(m):
        if ary[i][j]==2:
            start=(i,j)

visited=[[0]*m for _ in range(n)]
visited[start[0]][start[1]]=0
q=deque([start])
cnt=1
while q:
    for _ in range(len(q)):
        i, j = q.popleft()
        # print(q)

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == 0 and ary[ni][nj] == 1:
                visited[ni][nj] = cnt
                q.append((ni, nj))
    else:
        cnt += 1

visited[start[0]][start[1]]=0

for i in range(n):
    for j in range(m):
        if visited[i][j]==0 and ary[i][j]==1:
            visited[i][j]=-1


for x in visited:
    a=list(map(str,x))
    print(' '.join(a))