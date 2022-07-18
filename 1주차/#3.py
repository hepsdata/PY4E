📌Q3. 파이썬은 우리의 명령을 이해하지 못했을 때, 친절하게 Error Message를 통해
     어떤 명령을 이해하지 못했는지 알려줍니다. 그것을 보고 코드의 버그를 수정해가는 과정을
     Debugging이라고 합니다. 이것은 코딩에 있어서 매우 중요합니다.
     따라서, Error Message에 대해서 이해하는 시간을 가져봅시다.
     강의에서는 SyntaxError, ValueError, TypeError 3가지가 등장했습니다.

    ①각각의 Error를 발생시키는 코드를 2가지씩 만들어보고
    ②Debugging한 코드도 만들어 봅시다.
    ③그리고 그 밖에 다른 Error도 3가지를 찾아 그 Error를 발생시키는 코드와
    ④Debugging한 코드를 1가지씩 만들어 봅시다.

    #1.synataxError (구문오류)
    #파이썬 문법을 지키지 않으면 에러
1    print hello world

2    for i in range(5)
        print(i)

    #1.synataxError Debugging
    #예약어 끝에 콜론(:)이 있는지 확인
    #range()는 특정 구간의 숫자의 범위를 만듬
1    print('hello world')

2    for i in range(5):
        print(i)

    #2.ValueError (값오류)
    #int()와 float에 정수가 아닌 문자열을 입력하면 에러
    #문자열을 입력하려면 str() 사용
    #문자열은 '으로 시작하면 '로 끝나고 "로 시작하면 "로 끝나야 함
3    print(int('7.23'))

4    print(float('hello world'))

    #2.ValueError Debugging
    #int()는 입력한 실수 및 정수로부터 정수까지 출력
    #float()는 입력한 실수로부터 소수점까지 출력
3    print(int(7.23))

4    print(float(9.999))

    #3.TypeError(타입오류)
    #데이터 타입으로 인한 에러
5    a = [1,2]
     b = "Hello"
     print(a+b)

6    print(1 + "a")

    #3.TypeError Debugging
    #리스트[]는 문자열""이 아닌 리스트[]와 결합가능
5    a = [1,2]
     b = [3,4]
     print(a+b)

6    print(1+20213)

    #4.ZeroDivisonError / Debugging
    #숫자를 0으로 나누려는 경우 에러
7   print(1238/0)

7   print(1238/2)

    #5.NameError / Debugging
    #변수의 이름을 찾을 수 없는 경우 에러
8   a = 1
    b = 2
    print(c)

8   a = 1
    b = 2
    print(a)

   #6.OverflowError / Debugging
   #산술 연산의 결과가 너무 클 때 에러
9  pow(2, 1_000_000)

9  print(pow(2, 4))
