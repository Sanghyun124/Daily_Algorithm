a,b=map(int,input().split())

GCD=0

for x in range(1, a+1 if a<b else b+1):
    if a%x==0 and b%x==0:
        GCD=x

print(GCD)
print(a*b//GCD)

