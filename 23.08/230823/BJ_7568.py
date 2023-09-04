n=int(input())
p=[]
for _ in range(n):
    p.append(list(map(int,input().split())))

cnt=[0]*n

for a in range(n):
    for b in range(n):
        if a!=b:
            if p[a][0]<p[b][0] and p[a][1]<p[b][1]:
                cnt[a]+=1

for d in cnt:
    print(d+1,end=" ")


