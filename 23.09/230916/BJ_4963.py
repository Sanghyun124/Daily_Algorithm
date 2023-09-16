import sys
from collections import deque

input = sys.stdin.readline

di=[0,1,1,1,0,-1,-1,-1]
dj=[1,1,0,-1,-1,-1,0,1]

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break

    given=[list(map(int,input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]

    cnt=0
    for i in range(h):
        for j in range(w):
            if given[i][j]==1 and visited[i][j]==0:
                visited[i][j]=1
                q=deque([[i,j]])
                while q:
                    now=q.popleft()

                    for d in range(8):
                        ni=now[0]+di[d]
                        nj=now[1]+dj[d]

                        if 0<=ni<h and 0<=nj<w and visited[ni][nj]==0 and given[ni][nj]==1:
                            visited[ni][nj] = 1
                            q.append([ni,nj])
                cnt+=1
    print(cnt)