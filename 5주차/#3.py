def guess_numbers() :

    import random

    #number : 정답 숫자 3개
    # 1부터 100까지의 범위중에 10개를 중복없이 뽑겠다.
    number = random.sample(range(1,101),3)
    #작은 수부터 나열하기 -> 비교를 위한
    number.sort()

    #이미 예측에 사용한 숫자 분별, answer에 number가 다 충족이 되면 끝내기
    answer = []

    #n차 시도
    n = 0

    while True:
        
        n += 1
        print(f"{n}차 시도")

        ans = input("숫자를 맞춰보세요 : ")
        print(f"숫자를 맞춰보세요 : {ans}")
        #int처리 해야함
        ans = int(ans)
        answer.append(ans)


        if ans in number :
            print(f"숫자를 맞추셨습니다.")
        elif ans in answer :
            print(f"{ans}는 이미 예측에 사용한 숫자입니다")
        elif number[0] > ans :
            print(f"{ans}는 없습니다.")
            print(f"최솟값은 {ans}보다 큽니다")
        elif number[0] < ans and number[1] < ans:
            print(f"{ans}는 없습니다.")
            print(f"최솟값은 {ans}보다 작습니다")
        elif number[1] < ans and number[2] > ans :
            print(f"{ans}는 없습니다.")
            print(f"최댓값은 {ans}보다 큽니다")
        else :
            print(f"{ans}는 없습니다.")
            print(f"최대값은 {ans}보다 작습니다")
            
        # 끝내기
        if number[0] in answer and number[1] in answer and number[2] in answer:
            print(f"정답을 다 맞췄습니다. / 정답 : {number}")
            break
        
guess_numbers()