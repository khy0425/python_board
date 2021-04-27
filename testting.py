Things = 10
while True:
    money = int(input("넣을 돈 : "))
    if money == 1300:
        print("음료를 드려요")
        Things = Things - 1
    elif money > 1300:
        print("거스름돈 : ", money - 1300, "음료를 드려요\n", )
        Things = Things - 1
    else:
        print("돈을 다시 돌려주고 음료도 안드려요.")
        print("남은 음료 == ", Things, "개.")
    if not Things:
        print("음료가 없어요. 판매 할 수 없습니다.")
        break
