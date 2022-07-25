#Q3. 학생 이름과 점수를 입력하면 학점을 출력하는 학점 변환기를 만들어 봅시다.
#이름과 점수, 학점 모두 출력하도록 해봅니다.
#아래의 학점표를 토대로 만들어주세요.

# 오프닝
print('★학점변환기: 점수를 입력하면 학점을 출력합니다.')
name = input("당신의 이름은?: ")
score = input("몇 점을 받았나요?: ")
score=int(score)

# 학점 계산
def grader(name,score):
    if score >= 95:
        return 'A+'
    elif score >= 90:
        return 'A'
    elif score >= 85:
        return 'B+'
    elif score >= 80:
        return 'B'
    elif score >= 75:
        return 'C+'
    elif score >= 70:
        return 'C'
    elif score >= 65:
        return 'D+'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# 출력
print("학생 이름 :",name)
print("점수 :",score,"점")
print("학점 :",grader(name, score))
