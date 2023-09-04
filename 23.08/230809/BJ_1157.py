# 'A' 65 'a' 97

s=list(input())
alphas=[0]*32
for x in s:
    if ord(x)>=97:
        alphas[ord(x) - 97]+=1
    else:
        alphas[ord(x) - 65] += 1

cnt=0
max_num=0

for n in alphas:
    if n>max_num:
        max_num=n
        cnt=1
    elif n==max_num:
        cnt+=1

if cnt>1:
    print('?')
else:
    print(chr(alphas.index(max_num)+65))