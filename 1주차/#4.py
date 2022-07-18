📌Q4. 강의에서 미국과 유럽의 엘리베이터 층수를 변환하는 프로그램이 나왔습니다.
      그와 비슷하게 우리는 한국 나이를 미국 나이로 변환하는 프로그램을 코딩 해봅시다.
      - hint: 미국 나이는 생일이 지났는지 안지났는지가 중요하죠!

A4.
print ("한국나이 ▶ 미국나이 변환 프로그램")

n_year = int(input('현재 년도 : '))
n_month = int(input('현재 달 : '))
n_day = int(input('현재 일 : '))
b_year = int(input('태어난 년도 : '))
b_month = int(input('태어난 달 : '))
b_day = int(input('태어난 일 : '))

if b_month < n_month :
    print('당신의 미국나이 : ', n_year - b_year, '세')

elif b_month == n_month :
    if b_day <= n_day :
        print('당신의 미국나이 : ', n_year - b_year, '세')
    else :
        print('당신의 미국나이 : ', n_year - b_year - 1, '세')

elif b_month > n_month :
    print('당신의 미국나이 : ', n_year - b_year - 1, '세')
