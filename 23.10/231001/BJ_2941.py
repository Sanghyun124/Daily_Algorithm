s=input()
alphas=['c','d','l','n','s','z']
p=0
cnt=0
l=len(s)
while p<l:
    if l-p>1:
        if s[p]=='c':
            if s[p+1]=='-' or s[p+1]=='=':
                p+=2
                cnt+=1
                continue
        if s[p]=='d':
            if s[p+1]=='-':
                p+=2
                cnt+=1
                continue
            if l-p>2 and s[p+1]=='z' and s[p+2]=='=':
                p+=3
                cnt+=1
                continue
        if s[p] in ['l','n'] :
            if s[p+1]=='j':
                p += 2
                cnt += 1
                continue
        if s[p] in ['s','z']:
            if s[p + 1] == '=':
                p += 2
                cnt += 1
                continue
    cnt+=1
    p+=1
print(cnt)