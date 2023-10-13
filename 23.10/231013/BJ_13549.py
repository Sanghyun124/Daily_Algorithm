import sys,heapq

input = sys.stdin.readline

n,m,k,x=map(int,input().split())

node=[[] for _ in range(n+1)]
INF=1e9
d=[INF]*(n+1)
q=[]
d[x]=0
heapq.heappush(q,(0,x))
for _ in range(m):
    a,b=map(int,input().split())
    node[a].append((1,b))

while q:
    nw,now = heapq.heappop(q)

    if nw<d[now]:
        continue

    for w,next in node[now]:
        W=w+nw

        if W<d[next]:
            d[next]=W
            heapq.heappush(q,(W,next))

flag=1
for x in range(n+1):
    if d[x]==k:
        print(x)
        flag=0
if flag:
    print(-1)