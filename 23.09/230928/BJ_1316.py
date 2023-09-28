import sys

input = sys.stdin.readline

n=int(input())
cnt=0
for _ in range(n):
    s=input().rstrip()
    flag=0
    temp=[]
    last=''
    for w in s:
        if w not in temp:
            last=w
            temp.append(w)
        else:
            if w!=last:
                flag=1
        # print(temp)

    if not flag:
        cnt+=1
    # print(cnt)
print(cnt)
