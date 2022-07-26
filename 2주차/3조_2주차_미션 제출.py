##########################################################################
# Q1
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
rcpWinner(input('What''s your choice rock,cissor or paper???'))

##########################################################################
# Q2
# yearly_payment(payment) : 인자로 세전연봉을 넣으면 세후 연봉을 계산하여 리턴하는 함수
def yearly_payment(payment) :
    # 세율 변수 선언
    tax_rate = 0
    # 세전연봉별 세율 설정
    if payment <= 1200 : 
        tax_rate = 0.06
    elif payment <= 4600 :
        tax_rate = 0.15
    elif payment <= 8800 :
        tax_rate = 0.24
    elif payment <= 15000 :
        tax_rate = 0.35
    elif payment <= 30000 :
        tax_rate = 0.38
    elif payment <= 50000 :
        tax_rate = 0.40
    else :
        tax_rate = 0.42
    #세후연봉계산
    real_payment = payment * (1 - tax_rate)
    #결과값 리턴
    return int(real_payment)


# 월급입력
monthly_payment  = int(input('월급을 입력해주세요.'))

# 세전연봉, 세후연봉 변수 선언 및 할당
salary_before_tax = monthly_payment * 12
salary_after_tax = yearly_payment(salary_before_tax)

# 출력
print('세전연봉: '+str(salary_before_tax) +'만원')
print('세후연봉: '+str(salary_after_tax)+'만원')

##########################################################################
# Q3
# grade(name,score) : 이름과 성적을 인자로 받으면 이름, 성적, 학점을 출력하는 함수
def grade(name, score) :
    # 학점 변수 선언
    grade = ''
    if score >= 95 and score <= 100 : 
        grade = 'A+'
    elif score >= 90 and score < 95 : 
        grade = 'A'
    elif score >= 85 and score < 90 : 
        grade = 'B+'
    elif score >= 80 and score < 85 : 
        grade = 'B'
    elif score >= 75 and score < 80 : 
        grade = 'C+'
    elif score >= 70 and score < 75 : 
        grade = 'C'
    elif score >= 65 and score < 60 : 
        grade = 'D+'
    elif score >= 60 and score < 65 : 
        grade = 'D'
    elif score >=0 and score < 60 :
        grade = 'F'
    else : 
        # 학점을 계산할 수 없는 성적의 입력 : 강제종료
        print('학점을계산할 수 없습니다. 점수는 0~100 사이만 입력 가능합니다')
        return
    
    # 출력
    print('학생이름 : '+name)
    print('점수 : '+str(score))
    print('학점 : '+grade)
    

# 이름과 점수 입력( + 예외처리)
try : 
    strName = str(input('이름을 입력해주세요'))
    intScore = int(input('점수를 입력해주세요'))
except : 
    print('잘못된 입력입니다.종료합니다')
    exit()

# 출력
grade(strName, intScore)

##########################################################################
# Q4
# grade(name,score) : 나이와 지불수단을 인자로 받으면 나이, 지불유형, 버스요금을 출력하는 함수
def bus_fare(age, payment) :
    # 버스요금 변수 선언
    fare = 0   
  
    # 지불수단 예외처리 
    if payment != '카드' and payment != '현금' : 
      print('지불수단을 잘못 입력했습니다. 카드나 현금만 입력해주세요')
      # 강제종료
      return
    # 나이 예외처리
    if age < 0 : 
      print('나이를 잘못 입력했습니다. 나이는 0세 이상만 입력가능합니다.')
      # 강제종료
      return
      
    # 버스요금 산정
    if age >= 8 and age < 14 :
      fare = 450
    elif age >= 14 and age < 20 :
      fare = 1000
      if payment == '카드' : 
        fare -= 180      
    elif age >= 20 and age <75 : 
      fare = 1300
      if payment == '카드' : 
        fare -= 100  
      
      
    
    # 출력
    print('나이 : '+str(age))
    print('지불유형 : '+payment)
    print('버스요금 : '+str(fare)+'원')
    

# 나이와 지불수단 입력( + 예외처리)
try : 
    intAge = int(input('나이를 입력해주세요. 숫자만 입력 가능합니다.'))
    strPayMethod = str(input('지불수단을 입력해주세요. "카드" 나 "현금" 중에만 입력할 수 있습니다.'))
except : 
    print('잘못된 입력입니다.종료합니다')
    exit()

# 출력
bus_fare(intAge, strPayMethod)

##########################################################################