import sys, heapq

input = sys.stdin.readline

n=int(input())
q=[]
for _ in range(n):
    # print(q)
    t=int(input())
    if t:
        heapq.heappush(q,(abs(t),t))
    else:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)