def factorial(n):
    total=1
    for i in range(1,n+1):
        total=total*i
    return total

T=int(input())

for i in range(0,T):
    a,b=map(int,input().split())
    ans=int(factorial(b)/(factorial(a)*factorial(b-a)))
    print(ans)