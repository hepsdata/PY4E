  
#Q1. 여러분 혹시 베스킨라빈스31 게임을 아시나요? 1부터 31까지 숫자를 플레이어들끼리 번갈아 외치다가 31을 외치는 사람이 패배하는 게임인데요.
#이번엔 이 게임을 파이썬 함수로 만들어 봅시다. 지성이 없이 숫자를 랜덤하게 외치는 컴퓨터와 대결을 해보겠습니다.
#😲조건1 - 나의 턴에서는 숫자를 직접 입력하며 한 번 입력 후에 space 한 번으로 구분
#😲조건2 - 나와 컴퓨터 모두 한 턴에 1회 ~ 3회까지만 숫자를 외칠 수 있음
#😲조건3 - 외쳐진 숫자보다 1큰 수만 외칠수 있음 (ex: 5 다음엔 무조건 6)
  
 
  
  def bs31():
    print("베스킨라빈스 써리원 게임")
    print("------------------")
    import random
    number = 0
    while True:
        # my turn
        my = input("My turn - 숫자를 입력하세요: ")
        my = my.split()
        if int(my[0]) != number + 1 or len(my) > 3:
            print("숫자를 제대로 입력하세요")
            continue
        # 숫자 2개 입력 후 연속된 숫자가 아닐 경우 제한
        if len(my) == 2:
            if int(my[1]) - int(my[0]) != 1:
                print("연속된 숫자만 입력하세요")
                continue
        # 숫자 3개 입력 후 연속된 숫자가 아닐 경우 제한
        if len(my) == 3:
            if int(my[2]) - int(my[1]) != 1 or int(my[1]) - int(my[0]) != 1:
                print("연속된 숫자만 입력하세요")
                continue
 
 
        number = int(my[-1])
        print(f"현재 숫자 : {number}")
 
        # 31을 넘겼는지 검사
        if number >= 31:
            print("패배")
            break
 
        # computer
        computer = []
        computer_turn_num = random.randint(1,3)
        for i in range(computer_turn_num):
            number += 1
            # 컴퓨터가 31이 넘는 수를 외치면 31로 되돌리기
            if number > 31:
                number = number - 1
                continue
            computer.append(number)
            print(f"컴퓨터 : {computer[-1]}")
        print(f"현재 숫자 : {number}")
        print()
        # 31이 있는지 검사
        if 31 in computer:
            print("승리!")
            break
    print("게임 종료")
