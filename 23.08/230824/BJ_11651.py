import sys

input=sys.stdin.readline

n=int(input())
points=[list(map(int,input().split())) for _ in range(n)]
points.sort(key=lambda x:x[0])
points.sort(key=lambda x:x[1])

for x in points:
    print(f'{x[0]} {x[1]}')
