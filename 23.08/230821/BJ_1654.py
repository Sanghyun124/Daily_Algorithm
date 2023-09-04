import sys

input=sys.stdin.readline

k,n=map(int,input().split())
wires=[int(input()) for _ in range(k)]

r=max(wires)
l=1

while l<=r:
    temp = (r + l) // 2
    res=0
    for x in wires:
        res+= (x//temp)
    if res>=n:
        l=temp+1
    else:
        r=temp-1

print(r)