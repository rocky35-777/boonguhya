class BreadShop:
    def __init__(self):
        self.stock = {    #key값을 이용해서 value값을 찾을 수 있다. 딕셔너리는 스토리가 있다. 
        # 어떤 스토리 기반으로 데이터가 구성되어 있을때 딕셔너리를 사용한다. 
        "팥붕어빵" : 10, 
        "슈크림붕어빵" : 8,
        "초코붕어빵" : 5, #마지막엔 ,콤마 유무 상관없으나 시인성 높이기 위해 찍는 사람 있음
        }   

        self.sales = {    
        "팥붕어빵" : 0, 
        "슈크림붕어빵" : 0,
        "초코붕어빵" : 0
        }

        self.price = {
            "팥붕어빵" : 1000,
            "슈크림붕어빵" : 1500,
            "초코붕어빵" : 2000
        }

    def order_bread(self):
        while True : 
            bread_type = input("메뉴를 선택해 주세요.(팥붕어빵, 슈크림붕어빵, 초코붕어빵) 처음화면으로 가시려면 취소버튼을 눌러주세요.")
            if bread_type == "취소" :
                print("처음화면으로 돌아갑니다.")
                break
            if bread_type in self.stock : 
                bread_count = int(input("수량을 입력하세요."))
                if self.stock[bread_type] >= bread_count :
                    self.stock[bread_type] -= bread_count
                    self.sales[bread_type] += bread_count
                    print(f"{bread_type} {bread_count} 개가 선택되었습니다.")
                else :
                    print(f'{self.stock[bread_type]} 개만 주문 가능합니다.')
            else :
                print("다시 선택해 주세요.🙏🏻")
            
        # stock[bread_type] = stock[bread_type] -= bread_count # i = i + 1 / i += 1
        # 딕셔너리에 키값을 넣어서 실행하면? 벨류가 나옴, = 할당
        # 주문한 개수를 stock에서 빼줘야 함.
         

# 붕어빵 admin 기능 
    def admin_mode(self):
        while True :
            bread_type = input("주문할 메뉴를 선택해 주세요. 주문할 메뉴가 없다면 뒤로가기 버튼을 눌러주세요.")
            if bread_type == "뒤로가기" :
                print("이전화면으로 돌아갑니다.")
                break
            if bread_type in self.stock :
                bread_count = int(input("창고에 채워넣을 개수를 입력하세요:")) #8
                self.stock[bread_type] += bread_count
                print(f"{bread_type}의 재고가 {bread_count} 개 추가되어, 현재 총 {self.stock[bread_type]}개 입니다.")
            else :
                print("다시 선택해 주세요.🙏🏻")

# 붕어빵 계산 기능
    def caculate_sales(self):
        # total_sales = sum(sales[key] * price[key] for key in sales) #딕셔너리를 for문에 넣으면 하나씩 데이터를 가져오는데 이 데이터는 키값
        total = 0 #토탈이 0이어서 매번 초기화가 될 것이다. 
        for key in self.sales:
            total += (self.sales[key] * self.price[key])
        print(f"오늘의 총 매출은 {total}원 입니다.")