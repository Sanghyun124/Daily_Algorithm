t=int(input())
for _ in range(t):
    h,w,n=map(int,input().split())
    if n%h:
        height=n%h
        room = str(n//h+1) if (n//h+1)>9 else '0'+str(n//h+1)
    else:
        height = h
        room = str(n//h) if n//h>9 else '0'+str(n//h)
    print(str(height)+room)
