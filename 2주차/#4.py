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
