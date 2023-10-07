import sys,heapq

input = sys.stdin.readline
INF = sys.maxsize
V,E=map(int,input().split())
k=int(input())
d=[INF]*(V+1)
q=[]
g=[[] for _ in range(V+1)]

def dijkstra(start):
    d[start]=0
    heapq.heappush(q,(start,0))

    while q:
        now,nW=heapq.heappop(q)

        if d[now]<nW:
            continue

        for next,w in g[now]:
            nextW=w+nW
            if nextW<d[next]:
                d[next] = nextW
                heapq.heappush(q,(next,nextW))
for _ in range(E):
    u,v,w=map(int,input().split())
    g[u].append((v,w))
dijkstra(k)
for i in range(1,V+1):
    print("INF" if d[i] == INF else d[i])

