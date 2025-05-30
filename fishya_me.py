# for 는 반복횟수를 정할 수 있음 
"""for i in 반복할 횟수가 들어있는 데이터
range, list[]

장점은 횟수를 고민할 필요 없음.
단점은 더 하고 싶어도 데이터 만큼만 반복되기 때문에 설정을 더 해줘야 한다. 
정해진 횟수 실행하기 좋음

while 조건만되면 계속한다, 무한굴례 (특정 조건에 만족할 떄까지...)
"""

# 주문, 관리자, 종료 이 3가지 선택을 통해서 각각 기능이 작동되도록 만들자. 

# input()을 통해서 3가지 중 한가지를 입력받아서 작동시킬 수 있음. 

# i = 0
# while i < 10 : 
#     mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료):")
#     i += 1 # i = i + 1

# while i < 10 : 
#     mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료):")
#     break


stock = {    #key값을 이용해서 value값을 찾을 수 있다. 딕셔너리는 스토리가 있다. 
    # 어떤 스토리 기반으로 데이터가 구성되어 있을때 딕셔너리를 사용한다. 
    "팥붕어빵" : 10, 
    "슈크림붕어빵" : 8,
    "초코붕어빵" : 5, #마지막엔 ,콤마 유무 상관없으나 시인성 높이기 위해 찍는 사람 있음
}

sales = {    
    "팥붕어빵" : 0, 
    "슈크림붕어빵" : 0,
    "초코붕어빵" : 0
}

def order_bread():
    while True : 
        bread_type = input("메뉴를 선택해 주세요.(팥, 슈크림, 초코) 처음화면으로 가시려면 취소버튼을 눌러주세요.")
        print(bread_type)
        if bread_type == "취소" :
            print("처음화면으로 돌아갑니다.")
            break
        # elif bread_type in ["팥", "슈크림", "초코"] :
        #     print("수량을 선택해 주세요")
        #     break
        bread_count = int(input("수량을 입력하세요."))
        if stock[bread_type] >= bread_count : 
            print(f"{bread_count} 개가 선택되었습니다.")
        elif bread_count > stock[bread_type] - bread_count :
            print(f'{stock[bread_type]} 개만 주문할 수 있습니다.')
            
        # stock[bread_type] = stock[bread_type] -= bread_count # i = i + 1 / i += 1
        # 딕셔너리에 키값을 넣어서 실행하면? 벨류가 나옴, = 할당
        # 주문한 개수를 stock에서 빼줘야 함.
         

while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료):") #주문
    # mode = "종료"
    if mode == "종료":
        print("시스템이 종료되었습니다.") # 가독성 좋음 
        break
    
    elif mode == "관리자":
        admin_bread()
    
    elif mode == "주문":
        order_bread()    
