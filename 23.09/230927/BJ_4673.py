ary=[0]*10001
n=1
while n<10000:
    temp=sum(list(map(int,list(str(n)))))+n
    if temp<10001:
        ary[temp]=1
    n+=1
for i in range(1,10001):
    if not ary[i]:
        print(i)