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
