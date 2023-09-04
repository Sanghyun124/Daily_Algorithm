import sys

input=sys.stdin.readline


n=int(input())
ary=[0 for _ in range(21)]
for _ in range(n):
    s=list(input().split())
    if s[0]=='add':
        ary[int(s[1])]=1
    if s[0]=='remove':
        if ary[int(s[1])]:
            ary[int(s[1])]=0
    if s[0]=='check':
        if ary[int(s[1])]:
            print(1)
        else:
            print(0)
    if s[0]=='toggle':
        ary[int(s[1])]=0 if ary[int(s[1])] else 1
    if s[0]=='all':
        ary=[1 for i in range(21)]
    if s[0]=='empty':
        ary=[0 for i in range(21)]
    # print(ary)