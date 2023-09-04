n=int(input())
p=[]
for _ in range(n):
    temp=list(input().split())
    temp[0]=int(temp[0])
    p.append(temp)
sorted_p=sorted(p,key=lambda x : x[0])
for x in sorted_p:
    print(x[0],x[1])