n=int(input())
start=1
t=1
while start<=n:
    start+=t
    t+=1


print(start-t+1,t)
if t%2:
    print(str(1+(n-(start-t+1)))+'/'+str(t-(1+(n-(start-t+1)))))
else:
    print(str(t - (1 + (n - (start - t + 1)))) + '/' +str(1 + (n - (start - t + 1))))