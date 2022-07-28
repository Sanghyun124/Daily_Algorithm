# 여기에 필요한 모듈을 추가합니다.
import random
import json


class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        self.number_lines=[]

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        for i in range(5):
            self.number_lines.append(list(sorted(random.sample(range(1,46),6))))


    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        print('=============================================')
        print(f'            제 {draw_number} 회 로또         ')
        print('=============================================')
        print(f'추첨일 : {self.get_draw_date(draw_number)[0]}/{self.get_draw_date(draw_number)[1]}/{self.get_draw_date(draw_number)[2]} (토)')
        print('=============================================')
        for i in range(0,len(self.number_lines)):
            print(f'{chr(65+i)} : {self.number_lines[i]}')

    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        print('=============================================')
        print(f'당첨 번호 : {self.get_lotto_numbers(draw_number)[0]} + {self.get_lotto_numbers(draw_number)[1]}')
        print('=============================================')
        for i in range(0,len(self.number_lines)):
            same_main_counts, is_bonus = self.get_same_info(self.get_lotto_numbers(draw_number)[0], self.get_lotto_numbers(draw_number)[1], self.number_lines[i])
            print(f'{chr(65+i)} : {same_main_counts}개 ',end='') 
            print('+ 보너스 일치', end='') if is_bonus==True else print('', end='') 
            print(f' ({self.print_rangking(self.get_ranking(same_main_counts, is_bonus))})')

    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        lotto_json = open(f'data/lotto_{draw_number}.json', encoding='UTF8')
        lotto_dict = json.load(lotto_json)
        year,month,day=lotto_dict["drwNoDate"].split('-')
        return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        lotto_json = open(f'data/lotto_{draw_number}.json', encoding='UTF8')
        lotto_dict = json.load(lotto_json)
        main_numbers=sorted(list(lotto_dict[i] for i in lotto_dict.keys() if ('drwtNo' in i) ))
        bonus_number=lotto_dict["bnusNo"]
        return main_numbers, bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        same_main_counts=0
        is_bonus=False
        for i in line:
            if i in main_numbers:
                same_main_counts+=1
            if i == bonus_number:
                is_bonus=True
        return same_main_counts, is_bonus
    # same_main_counts = len(set(main_numbers)&set(line))
    

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        ranking=0
        if same_main_counts==6:
            ranking=1
        elif same_main_counts==5:
            if is_bonus==True:
                ranking=2
            else :
                ranking=3
        elif same_main_counts==4:
            ranking=4
        elif same_main_counts==3:
            ranking=5
        else:
            ranking=-1
        return ranking

    @staticmethod
    def print_rangking(ranking):
        if ranking>0:
            return f'{ranking}등 당첨!'
        else:
            return '낙첨'
