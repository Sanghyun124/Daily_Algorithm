T = int(input())
for test_case in range(1, T + 1):
    print('#%d'%(test_case))
    N=int(input())
    string=[]
    for i in range(1,N+1):
        char, num=input().split()
        num=int(num)
        string+=(char*num)
    for k in range (0,len(string)) :
        if (k%10)==9 :
            print(string[k])
        else :
            print(string[k],end='')
    print()