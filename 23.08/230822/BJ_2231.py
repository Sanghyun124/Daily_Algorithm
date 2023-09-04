n=input()

l=len(n)

start=int(n)-9*l if int(n)-9*l>=0 else int(n)//2

while start<=int(n):
    temp=start
    # print(start)
    for x in list(str(start)):
        temp+=int(x)
        # print(start, temp)
    if temp==int(n):
        print(start)
        break
    else:
        start+=1
else:
    print(0)