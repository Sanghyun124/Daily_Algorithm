import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

di=[1,0,-1,0]
dj=[0,1,0,-1]

r,c=map(int,input().split())
alphas=[list(input()) for _ in range(r)]
maxLen=0

def dfs(start,track):
    global maxLen
    maxLen=max(maxLen,len(track))
    i,j=start

    for d in range(4):
        ni=i+di[d]
        nj=j+dj[d]
        if 0<=ni<r and 0<=nj<c and alphas[ni][nj] not in track:
            dfs((ni,nj),track+alphas[ni][nj])


dfs((0,0),alphas[0][0])

print(maxLen)