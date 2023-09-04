n=int(input())

cnt=0
num=1

while n>num:
    num+=cnt*6
    cnt+=1
else:
    print(1) if n==1 else print(cnt)