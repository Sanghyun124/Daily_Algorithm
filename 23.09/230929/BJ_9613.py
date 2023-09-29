import sys

input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

t=int(input())
for _ in range(t):
    ary=list(map(int,input().split()))
    n=ary[0]
    nums=ary[1:]
    res=0
    for x in range(n):
        for y in range(x+1,n):
            res+=gcd(nums[x],nums[y])
    print(res)