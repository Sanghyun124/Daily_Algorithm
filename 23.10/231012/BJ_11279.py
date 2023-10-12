import sys, heapq

input = sys.stdin.readline

n=int(input())
q=[]
for _ in range(n):
    t=int(input())
    if t:
        heapq.heappush(q,(-t,t))
    else:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)