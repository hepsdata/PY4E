#📌Q4. 오늘 애인이 생겼다고 해봅시다. 100일을 기념하고 싶은데요.
#날짜를 넣으면 100일 뒤가 몇월 며칠인지 계산해주는 함수를 만들어 보겠습니다.
#😲조건1 - "오늘부터 1일"이기 때문에 날짜를 계산할 때 오늘을 포함합니다
#😲조건2 - 몇년도인지 구분하지 않고 윤년도 고려하지 않고 2월은 무조건 28일로 합니다.

def after_100(month, date, day):
# 달 별로 며칠까지 있는지 리스트로 만들기
    dates = [31,28,31,30,31,30,31,31,30,31,30,31]
    # 요일 리스트
days = ["월","화","수","목","금","토","일"]
    after = 100
   
# 파이썬 index는 0부터 시작하기 때문에 월 -1
    index = month-1
   
    while True:
# 100일 음수가 될 때까지 날짜 차감
        after = after - dates[index]
        if after < 0:
            break
        # 12월 다음은 1월으로 돌아가기
        index = index + 1
        if index == 12:
            index = 0
 
# 음수가된 after에 100일 후의 월의 일수를 더해주고
# 현재 일 수를 더하고 오늘을 포함하기 때문에 -1
    date_after_100 = after + dates[index] + date -1
    # 만약 일수가 30일, 31일을 넘어가면 100일 후의 월의 일수를 빼주고 월 +1 추가 
if date_after_100 > dates[index]:
        date_after_100 = date_after_100 - dates[index]
        index = index + 1
    # 요일은 7로 나눈 나머지 만큼 움직이면 됨, 오늘을 포함하기 때문에 -1
day_index = days.index(day)
    day_index2 = day_index + 100 % 7 -1
# 일요일 다음은 월요일로 돌아감
    if day_index2 > (len(days) -1):
        day_index2 = day_index2 - (len(days) -1) -1
    day_after_100 = days[day_index2]    
   
    print(f"{month}월 {date}일 {day}요일부터 100일 뒤는 {index+1}월 {date_after_100}일 {day_after_100}요일"
