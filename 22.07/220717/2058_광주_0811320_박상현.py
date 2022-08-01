n=int(input())
sum=0
while n>9 :
    sum+=(n%10)
    n=n//10
sum+=n
print(sum)