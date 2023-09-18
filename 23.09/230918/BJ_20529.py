import sys

input = sys.stdin.readline

def compare(a,b,c):
    cnt=0
    for x in range(4):
        if a[x]!=b[x]:
            cnt+=1
    for x in range(4):
        if b[x]!=c[x]:
            cnt+=1
    for x in range(4):
        if a[x]!=c[x]:
            cnt+=1
    return cnt


t=int(input())
for _ in range(t):
    n=int(input())
    people=list(input().split())
    min_num=100000000000000000000000
    if n>32:
        print(0)
    else:
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    temp=compare(people[i],people[j],people[k])
                    min_num= temp if temp<min_num else min_num
        print(min_num)

