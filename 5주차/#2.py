# 학생 답
s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

# 정답지
a = [3,2,4,2,5,2,4,3,1,2]


def grader(s,a):
    
    
    sum_score = 0

    #이름과 답안지 나누기
    for i in range(0,len(s)):
        s[i] = s[i].split(",")

    #답안지의 각 문항별로 list형식으로 나누기
    #점수합계 list 추가
    for j in range(0,len(s)):
        s[j][1] = list(s[j][1])
        s[j][1] = list(map(int, s[j][1]))
        s[j].append(0)

    #1문제당 10점씩 더하기
    for k in range(0,len(s)):
        for g in range(0,9):
            if s[k][1][g] == a[g] :
                s[k][2] += 10
            else : continue

    #등수를 가리기 위해 score(합계점수) , rank(등수) 생성
    score = []
    rank = 0

    for c in range(0,len(s)):
        score.append(s[c][2])

    score.sort(reverse = True)          

    #score가 0번일수록 합계점수가 높음, ex) score[0] = 1등
    #rank += 1을 해서 점점 낮은 등수가 나오도록 함
    for r in range(0,len(score)):
        rank += 1
        for f in range(0,len(s)):
            if s[f][2] == score[r]:
                print("학생 :",s[f][0],", 점수 :",score[r],"점, ",rank,"등")
                
                
grader(s,a)