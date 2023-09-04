l=int(input())
s=list(input())
res=0
c=1
for i in range(l):
    res+=(ord(s[i])-96)*c
    c*=31

print(res%1234567891)


