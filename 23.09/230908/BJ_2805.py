import sys

input = sys.stdin.readline

n,m=map(int,input().split())
tree=list(map(int,input().split()))
l=0
r=max(tree)
mid=mid=(l+r)//2

while l<=r:
    temp=0
    mid=(l+r)//2
    for x in tree:
        temp+=(x-mid) if x-mid>=0 else 0
    print('l,r,mid,temp',l, r, mid, temp)
    if temp>=m:
        # if temp-m<n:
        #     break
        l=mid+1
    if temp<m:
        r=mid-1
print(r)