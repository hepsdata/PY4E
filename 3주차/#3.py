def find_even_number(firstNum, secondNum) : 
    numbers = range(firstNum, secondNum+1)
    middleNum = int((firstNum + secondNum) / 2)
    for i in numbers :
        if i % 2 == 0 :
            print(i, "짝수")
        if i == middleNum : 
            print(i, "중앙값")

try : 
    n = int(input("첫 번째 수 입력 : "))
    m = int(input("두 번째 수 입력 : "))
    find_even_number(n, m)
except :
    print("숫자를 입력해주세요.")
