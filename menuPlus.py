menu = ("콜라", "사이다", "환타", "물")
price = (800, 800, 700, 600)
money = 0
money = int(input("넣을 돈 : "))


def showMenu():
    print("자판기 메뉴")
    for i in range(0, len(menu)):
        print(i+1, ".", menu[i], "\t 가격 : ", price[i])


def buy(num):
    global money
    if money < price[num]:
        print("돈이 부족합니다. 잔액", money, "입니다.")
        return money
    else:
        print(menu[num], "구입")
        money = save - price[num]
        print("거스름 돈은 : ", money)
        return money


while True:
    save = money
    showMenu()
    Things = int(input("음료의 번호를 골라 주세요: (종료를 원하시면 : 0 를 눌러주세요) "))
    if Things == 0:
        break
    elif (Things >= 1 and Things <= len(menu)):
        money = buy(Things - 1)
    else:
        print("잘못된 선택입니다. 다시 입력하여 주십시오. \n")

print("감사합니다. 잔액은 : ", money, "입니다.")
