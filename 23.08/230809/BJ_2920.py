import copy

score=list(map(int,input().split()))
temp=copy.deepcopy(score)

if score==sorted(temp):
    print('ascending')
elif score==sorted(temp)[::-1]:
    print('descending')
else:
    print('mixed')

