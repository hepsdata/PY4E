def gugudan(danSu) : 
    print(str(danSu) + " 단")
    
    i = 0
    while i <= 9 :        
        i += 1
        if i % 2 == 0 :
            continue
        if danSu * i > 50 : 
            break
        print(str(danSu), 'X', str(i), '=', danSu * i)
    
#출력하기
try : 
    number = int(input("몇 단? : "))
    gugudan(number)
except : 
    print("단 수를 입력하세요. 숫자만 입력 할 수 있습니다.")
