import sys,copy

def count(ary,num,result):
    # print('num',num)
    if num==2:
        for x in range(num):
            for y in range(num):
                if ary[x][y]:
                    result[1] += 1
                else:
                    result[0]+=1
        return result
    else:
        # print('ary',ary)
        for x in range(2):
            for y in range(2):
                # print('(x,y)',x,y)
                temp=[[ary[i][j] for j in range((num//2)*y,(num//2)*(y+1))] for i in range((num//2)*x,(num//2)*(x+1))]
                # print('temp',temp)
                res=0
                for a in temp:
                    res+=sum(a)
                # print('res',res)
                if res==(num//2)**2:
                    # print(1)
                    result[1] +=1
                elif res == 0:
                    # print(0)
                    result[0]+=1
                else:
                    temp_result=count(copy.deepcopy(temp),num//2,[0,0])
                    result[0]+=temp_result[0]
                    result[1]+=temp_result[1]
                    # print('ary2',ary)
    return result

input = sys.stdin.readline

n=int(input())
paper=[list(map(int,input().split())) for _ in range(n)]

res=0
for a in paper:
    res += sum(a)
if res==n**2:
    print(0)
    print(1)
elif res==0:
    print(1)
    print(0)
else:
    res = count(paper,n,[0,0])
    for x in res:
        print(x)