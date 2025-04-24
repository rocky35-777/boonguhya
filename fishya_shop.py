from fishya_model import BreadShop
# 인스턴스화 시킴
shop = BreadShop()

# 붕어빵 main 화면
while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자, 종료):") #주문
    # mode = "종료"
    if mode == "종료":
        shop.caculate_sales()
        print("시스템이 종료되었습니다.") # 가독성 좋음 
        break
    
    elif mode == "관리자":
        shop.admin_mode()
    
    elif mode == "주문":
        shop.order_bread()    

# 로직이 숨겨지고, 로직을 별도로 관리함으로써 유지보수 용이해짐. 