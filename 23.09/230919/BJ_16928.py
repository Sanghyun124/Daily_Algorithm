import sys
from collections import deque

input = sys.stdin.readline


# Input 값 처리
n,m=map(int,input().split())

ladderDict={} # 사다리
snakeDict={} # 뱀

for _ in range(n):
    a,b=map(int,input().split())
    ladderDict[a]=b

for _ in range(m):
    a,b=map(int,input().split())
    snakeDict[a]=b

q=deque([(1,0)])
cnt=0
visited=[0]*101
visited[1]=1

while q:
    p,pCnt=q.popleft()
    if p in ladderDict.keys():
        p=ladderDict[p]
    if p in snakeDict.keys():
        p=snakeDict[p]
    if p == 100:
        print(pCnt)
        q = deque([])
        break
    for d in range(1,7):
        nP=p+d
        nPCnt=pCnt+1
        if nP<=100 and visited[nP]==0:
            visited[nP] = 1
            q.append((nP,nPCnt))

