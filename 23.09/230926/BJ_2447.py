def func(num):
    if num==3:
        return ['***','* *','***']
    else:
        ary=func(num//3)
        l=len(ary)
        newAry=[]
        for t in range(num):
            if t//(num//3)==1:
                    newAry.append(ary[t%l] + ' '*(num//3) + ary[t%l])
            else:
                    newAry.append(ary[t%l]*3)
        return newAry


n=int(input())
ans=func(n)
for x in ans:
    print(x)
