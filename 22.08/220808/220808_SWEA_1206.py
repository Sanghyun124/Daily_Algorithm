def find_max(num_list):
    max_num=0
    for num in num_list:
        max_num=num if max_num<num else max_num
    return max_num
 
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    house_len=int(input())
    house_list=list(map(int,input().split()))
     
    good_view=0
     
    for nth in range(2,house_len-2):
        check_view=house_list[nth-2:nth+3]
        if house_list[nth]==find_max(check_view):
            highest=find_max(check_view)
            check_view.remove(find_max(check_view))
            good_view+=(highest-find_max(check_view))
             
    print(f'#{test_case} {good_view}')
