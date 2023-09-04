from collections import deque

n,k=map(int,input().split())

q=deque([])
visited=[0]*100001

q.append(n)
visited[n]=1

cnt=0

while q:
    for _ in range(len(q)):
        now=q.popleft()
        if now==k:
            print(cnt)
            break
        else:
            if now+1<=100000 and visited[now+1]==0:
                q.append(now + 1)
                visited[now + 1] = 1
            if now - 1>=0 and visited[now-1]==0:
                q.append(now - 1)
                visited[now-1]=1
            if 0<now*2<=100000 and visited[now*2]==0:
                q.append(now * 2)
                visited[now*2]=1
    else:
        cnt+=1
        continue
    break
