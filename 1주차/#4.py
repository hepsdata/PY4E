j=0
while (j<1): # while loop
    try:
        age = 0 # reset
        age = int(input("당신은 몇 살 입니까? : ")) # input age

        j += 1
        i = 0
        
        while (i<1): # while loop
            try:
                birth_date = []
                today_date = []
                # reset

                birth_date = input('생일을 입력하세요 : ').split('/')
                today_date = input('오늘의 날짜를 입력하세요 : ').split('/')

                birth_date = [int(i) for i in birth_date]
                today_date = [int(i) for i in today_date]
                #정수형 변환하지 못할 때, exception 처리

                if (all([i>0 for i in birth_date]) and all([i>0 for i in today_date])) == True:
                    if (birth_date[0] > 13 or today_date[0] >13 ) or (birth_date[1] > 31 or today_date[1] > 31) :
                        print('잘못된 날짜입니다.\n')
                        i-=1 # while loop 반복 (날짜 재입력)
                    else :
                        i+=1 # while loop 종료 (날짜 재입력)
                else:
                    print('음수를 잘못 입력하셨습니다.\n')
                    i-=1 # while loop 반복 (날짜 재입력)

            except :
                print('잘못 입력하셨습니다.\n')
                i-=1 # while loop 반복 (날짜 재입력)

        if birth_date <= today_date: # 생일이 지났을 때
            #(birth_date[0] > today_date[0]) or ((birth_date[0] == today_date[0]) and (birth_date[1] < today_date[1])):
            factor = 0 # 그대로
        
        else: # 생일이 지나지 않았을 때
            factor = -1 # -1을 뺀다

        print("Your international age is " + str(age -1 + factor))

    except :
        print('나이를 잘못 입력하셨습니다.\n')
        j-=1 # while loop 반복 (나이 재입력)
