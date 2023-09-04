n,r,c=map(int,input().split())

ans=0
while n>0:
    # print(r,c,ans)
    if r>=2**(n-1):
        if c>=2**(n-1):
            ans+=((2**(n*2))//4)*3
            r-=2**(n-1)
            c-=2**(n-1)
        else:
            ans += ((2**(n*2))//4)*2
            r -= 2 ** (n - 1)
    else:
        if c>=2**(n-1):
            ans += ((2**(n*2))//4)
            c -= 2 ** (n - 1)
        else:
            ans += 0
    n=n-1

if r>0:
    if c>0:
        print(ans+3)
    else:
        print(ans+2)
else:
    if c>0:
        print(ans+1)
    else:
        print(ans)