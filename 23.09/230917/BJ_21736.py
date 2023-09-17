import sys
from collections import deque

input = sys.stdin.readline

di=[1,0,-1,0]
dj=[0,1,0,-1]


n,m=map(int,input().split())
ary=[list(input()) for _ in range(n)]

start=[0,0]
visited=[[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if ary[i][j]=='I':
            start=[i,j]
            visited[i][j]=1
            break
    else:
        continue
    break

cnt=0
q=deque([start])

while q:
    now=q.popleft()

    for d in range(4):
        ni=now[0]+di[d]
        nj=now[1]+dj[d]

        if 0<=ni<n and 0<=nj<m and visited[ni][nj]==0:
            if ary[ni][nj]=='X':
                continue
            if ary[ni][nj]=='P':
                cnt+=1
            q.append([ni, nj])
            visited[ni][nj]=1

if cnt:
    print(cnt)
else:
    print('TT')