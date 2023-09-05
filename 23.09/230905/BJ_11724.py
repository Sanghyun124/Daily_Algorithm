import sys

input=sys.stdin.readline


n,m=map(int,input().split())
p=[[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    p[u].append(v)
    p[v].append(u)
# print(p)
num=0
visited=[0 for _ in range(n+1)]
for x in range(1,n+1):
    if visited[x] == 0:
        visited[x] = 1
        num+=1
        stk=[x]
        while stk:
            now=stk.pop()
            for a in p[now]:
                if visited[a]==0:
                    visited[a]=1
                    stk.append(a)

print(num)