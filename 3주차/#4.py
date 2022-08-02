def count_prime_number(sNum, eNum) : 
    primeNumCnt = 0
    numbers = range(sNum, eNum+1)

    for num in numbers :
        # 공약수의 갯수를 세는 변수(값이 2이면 1과 자기자신만 약수로 가짐을 의미 : 소수)
        divisorCnt = 0
        for i in range(1, num+1) :
            #print("i===",i,"num===",num)
            if num % i == 0 :
                divisorCnt += 1
                #print("divisorCnt",divisorCnt)
            if num == 1 or (num == i and divisorCnt == 2) : 
                primeNumCnt += 1
    print("소수개수", str(primeNumCnt))
            
try : 
    n = int(input("첫 번째 수 입력 : "))
    m = int(input("두 번째 수 입력 : "))
    count_prime_number(n, m)
except :
    print("숫자를 입력해주세요.")
