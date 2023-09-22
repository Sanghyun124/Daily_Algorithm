import sys
from collections import deque

input = sys.stdin.readline


t=int(input())
for _ in range(t):
    a,b=map(int,input().split())

    nums = [0] * 10000
    q=deque([[a,'']])
    nums[a]=1

    while q:
        # print(q)
        now=q.popleft()
        n,s=now[0],now[1]

        if n==b:
            print(s)
            break

        nD=(n*2)%10000
        nS=n-1 if n!=0 else 9999
        nL=(n%1000)*10+(n//1000)
        nR=(n%10)*1000+(n//10)
        print(nD,nS,nL,nR)
        if not nums[nD]:
            nums[nD]=1
            q.append([nD,s+'D'])

        if not nums[nS]:
            nums[nS] = 1
            q.append([nS, s + 'S'])

        if not nums[nL]:
            nums[nL] = 1
            q.append([nL, s + 'L'])

        if not nums[nR]:
            nums[nR] = 1
            q.append([nR, s + 'R'])



