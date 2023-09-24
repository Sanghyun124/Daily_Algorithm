def find_gcp(a,b):
    gcp=0
    for x in range(1,a+1 if a>b else b+1):
        if a%x==0 and b%x==0:
            gcp=x
    return gcp




n=int(input())
gear=list(map(int,input().split()))
main=gear[0]
sub=gear[1:]
for x in sub:
    gcp=find_gcp(main,x)
    print(str(main//gcp)+'/'+str(x//gcp))