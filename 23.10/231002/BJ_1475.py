n=input()
nums=[0]*10
for x in n:
    if x not in ['6','9']:
        nums[int(x)]+=1
    else:
        if nums[6]<=nums[9]:
            nums[6]+=1
        else:
            nums[9]+=1
print(max(nums))