from collections import deque

n,k=map(int,input().split())

q=deque([i for i in range(1,n+1)])

ans=[]

for _ in range(n):
    print(q)
    q.rotate(-k)
    ans.append(q.pop())


print('<',end='')
for x in range(n):
    if x==n-1:
        print(ans[x],end='')
    else:
        print(f'{ans[x]},',end=' ')
print('>')
