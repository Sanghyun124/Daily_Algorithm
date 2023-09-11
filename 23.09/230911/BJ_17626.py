n=int(input())
nums=[0]*(n+1)
square_list=[i*i for i in range(1,316)]
now=1
for x in range(1,n+1):
    if x in square_list:
        nums[x]=1
    else:
        nums[x] = min([nums[x-y] for y in square_list if x-y > 0])+1

print(nums[n])