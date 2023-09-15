s=input().split('-')

ans=0

for x in range(len(s)):
    temp=s[x].split('+')
    temp_num=0
    for n in temp:
        temp_num+=int(n)
    if x==0:
        ans+=temp_num
    else:
        ans-=temp_num

print(ans)