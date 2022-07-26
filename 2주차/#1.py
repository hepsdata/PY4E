# 랜덤함수 임포트
import random

# rcpWinner(deci) : 사용자, 컴퓨터의 입력과, 가위바위보 게임의 승자를 출력하는 함수
def rcpWinner(deci) : 
    # 컴퓨터의 입력 : 컴퓨터의 입력으로 0~2(0:가위,1:바위,2:보)중 하나를 선택하게 함
    com = random.randint(0,2)
    
    # 사용자의 입력 : 사용자의 입력 예외처리 (6가지 경우만 입력 가능하도록) - 조건1
    try :
        my = int(deci)
        if my > 2 :
            print('You entered the wrong input. choose between 0, 1, 2')
            #강제종료
            return
    except : 
        if deci == "가위" : 
            my = 0
        elif deci == "바위" : 
            my = 1
        elif deci == "보" : 
            my = 2
        else :
            print('You entered the wrong input. choose between "가위","바위","보"')
            #강제종료
            exit()     
    
    # 결과 출력용 변수 설정 : 0 - 가위, 1 - 바위, 2 - 보
    strCom, strMy = ""
    if com == 0 :
        strCom = "가위"
    elif com == 1 : 
        strCom = "바위"
    elif com == 2 : 
        strCom = "보"
        
    if my == 0 :
        strMy = "가위"
    elif my == 1 : 
        strMy = "바위"
    elif my == 2 : 
        strMy = "보"
    
    # 가위바위보 승리자 판단로직(숫자가 같음 = 비김, 다름 = 승패갈림)
    #승패결과를 담는 변수(문자열)
    strWinner = ''

    # 같은 입력을 내면 비김
    if com == my : 
      strWinner = 'DRAW~~~~~~~~'
    # 컴퓨터의 입력을 기준으로 승패 판단
    else : 
      # 컴퓨터 = 가위
      if com == 0 : 
        # 사용자 = 바위
        if my == 1 :
          strWinner = 'Winner is YOU:-)'                  
        # 사용자 = 보
        elif my == 2 :
          strWinner = 'Winner is Computer:-('
          
      # 컴퓨터 = 바위
      elif com == 1 :
        # 사용자 = 가위
        if my == 0 :
          strWinner = 'Winner is Computer:-('
        # 사용자 = 보
        elif my == 2 :
          strWinner = 'Winner is YOU:-)'                  
  
      #컴퓨터 = 보
      else :
        # 사용자 = 가위
        if my == 0 :
          strWinner = 'Winner is YOU:-)'                  
        # 사용자 = 바위
        elif my == 1 :
          strWinner = 'Winner is Computer:-('

    # 출력
    print("나: "+strMy)
    print("컴퓨터: "+strCom)
    print("결과: "+strWinner)


#실행
rcpWinner(input('What''s your choice rock,cissor or paper?'))
