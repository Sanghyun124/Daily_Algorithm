n=int(input())

points=[]

for _ in range(n):
    points.append(list(map(int,input().split())))

points.sort(key=lambda x:x[1])
points.sort(key=lambda x:x[0])

for x in points:
    print(x[0],x[1])