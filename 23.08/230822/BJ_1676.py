import math

n=int(input())

num=math.factorial(n)
cnt=0

while num%10==0:
    cnt+=1
    num=num//10

print(cnt)



