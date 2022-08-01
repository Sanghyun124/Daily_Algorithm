T = int(input())
for test_case in range(1, T + 1):
    M,N = map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    ans=[]
    if M<N :
        for i in range(0,abs(M-N)+1):
            temp=0
            for j in range(0,M):
                temp+=(A[j]*B[j+i])
            ans.append(temp)
    else :
        for i in range(0,abs(M-N)+1):
            temp=0
            for j in range(0,N):
                temp+=(A[j+i]*B[j])
            ans.append(temp)
    print('#%d %d'%(test_case,max(ans)))