import sys

input = sys.stdin.readline

n,m=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(n)]

di=[[0,0,0,0],[0,1,2,3],[0,0,1,1],[0,1,2,2],[0,1,2,2],[0,0,0,1],[0,0,0,-1],[0,0,1,2],[0,0,1,2],[0,1,0,0],[0,-1,0,0],
    [0,1,1,2],[0,1,1,2],[0,0,1,1],[0,0,-1,-1],[0,0,1,0],[0,1,1,2],[0,0,-1,0],[0,1,1,2]]
dj=[[0,1,2,3],[0,0,0,0],[0,1,0,1],[0,0,0,1],[0,0,0,-1],[0,1,2,2],[0,1,2,2],[0,1,0,0],[0,-1,0,0],[0,0,1,2],[0,0,1,2],
    [0,0,1,1],[0,0,-1,-1],[0,1,1,2],[0,1,1,2],[0,1,1,2],[0,0,1,0],[0,1,1,2],[0,0,-1,0]]

max_num=0


for i in range(n):
    for j in range(m):
        for x in range(19):
            temp=0
            cnt=0
            for d in range(4):
                ni = i + di[x][d]
                nj = j + dj[x][d]
                if 0<=ni<n and 0<=nj<m:
                    temp+=maps[ni][nj]
                    cnt+=1
                else:
                    break
            if cnt==4:
                max_num=temp if temp>max_num else max_num

print(max_num)



### DFS로 풀수 있다...
# 진짜 천재들 많네..