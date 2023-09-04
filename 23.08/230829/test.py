num=int(input())
ary=[list(map(int,input().split()))]
print(ary)
for x in range(2):
    for y in range(2):
        temp=[[(i,j) for j in range((num//2)*y,(num//2)*(y+1))] for i in range((num//2)*x,(num//2)*(x+1))]
        print(temp)

