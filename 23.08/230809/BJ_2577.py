a=int(input())
b=int(input())
c=int(input())

nums=[0]*10

for x in list(str(a*b*c)):
    nums[int(x)]+=1

for x in nums:
    print(x)