import sys

input=sys.stdin.readline

n,m,b=map(int,input().split())
map=[list(map(int,input().split())) for _ in range(n)]

min_time=256*2*n*m+1
height=0

for i in range(257):
    use=0
    take=0
    for x in range(n):
        for y in range(m):
            if map[x][y]>i:
                take +=map[x][y]-i
            else:
                use +=i-map[x][y]
    if use > take+b:
        continue

    time = take * 2 + use

    if time<=min_time:
        min_time=time
        height=i

print(min_time, height)

