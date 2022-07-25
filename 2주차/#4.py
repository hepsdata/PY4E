#Q4. 나이와 현금 또는 카드를 입력하면 버스 요금이 출력되는 버스 요금 계산기를 만들어봅시다. 
#아래의 요금표를 토대로 만들어주세요.
#8세미만(카드/현금:무료), 8세이상~14세미만(카드/현금:450원), 14세 이상~20세미만(카드:720원/현금:1000원)
#20세이상(카드:1200원/현금:1300원), 75세이상(카드/현금:무료)

#오프닝
print('★ 버스요금계산기: 나이와 지불방법을 입력해보세요.')
age = input("당신의 나이는?: ")
pay = input("지불방법(카드/현금)은?: ")
age = int(age)

# 버스 요금 계산식
def bus_fare(age, payment):
    if payment == '카드':
        if age < 8:
           return '무료'
        elif age < 14:
            return '450원'
        elif age < 20:
            return '720원'
        elif age < 75:

            return '1200원'
        else :
            return '무료'
    else:
        if age < 8:
               return '무료'
        elif age < 14:
            return '450원'
        elif age < 20:
            return '1000원'
        elif age < 75:
            return '1300원'
        else :
            return '무료'

print('버스요금 계산결과:')
print('나이:',age)
print('지불유형:',pay)
print('버스요금:',bus_fare(age, pay))
