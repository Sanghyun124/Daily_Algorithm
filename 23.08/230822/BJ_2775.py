from copy import deepcopy

t=int(input())

for _ in range(t):
    k=int(input())
    n=int(input())
    init=[i for i in range(n+1)]
    for _ in range(k):
        temp=[]
        num=0
        for x in init:
            num+=x
            temp.append(num)
        init=deepcopy(temp)
    print(init[n])
