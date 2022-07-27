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
