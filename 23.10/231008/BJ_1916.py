import sys,heapq

input = sys.stdin.readline

n=int(input())
m=int(input())
g=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,w=map(int,input().split())
    g[a].append((w,b))

A,B=map(int,input().split())
INF=1e9
d=[INF]*(n+1)
d[A]=0
q=[]


def dijkstra(start):
    heapq.heappush(q, (0, start))
    while q:
        now_w, now = heapq.heappop(q)

        if d[now]<now_w:
            continue

        for w,next in g[now]:
            next_w=now_w+w
            if next_w<d[next]:
                d[next]=next_w
                heapq.heappush(q,(next_w,next))

dijkstra(A)
print(d[B])