T = int(input())
for test_case in range(1, T + 1):
    string=input()
    check=0
    if string==string[::-1] :
        check=1
    else:
        check=0
    print('#%d %d'%(test_case,check))