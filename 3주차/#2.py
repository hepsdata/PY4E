# 랜덤함수 임포트
import random

# rspWinner(time) : 사용자 입력과 게임 회차를 매개변수로 받아 게임의 결과와 승자를 출력하는 함수
def rspWinner(time) : 
    # 컴퓨터의 입력 : 컴퓨터의 입력으로 0~2(0:가위,1:바위,2:보)중 하나를 선택하게 함
    com = random.randint(0,2)
    my = userRsp()
    # 결과 출력용 변수 설정 : 0 - 가위, 1 - 바위, 2 - 보
    strCom, strMy = '', ''
    strCom = convertNumToRsp(com)
    strMy = convertNumToRsp(my)
    
    # 가위바위보 승리자 판단로직(숫자가 같음 = 비김, 다름 = 승패갈림)
    # 승패결과를 담는 변수(문자열)
    strWinner = ''
    # 결과카운터 변수(0 = 비김, 1 = 내승리, 2 = 컴퓨터승리)
    intRes = 0

    # 같은 입력을 내면 비김
    if com == my : 
        strWinner = "비김~~"
    # 승패경우 판단
    else : 
        if (com == 0 and my == 1) or (com == 1 and my == 2) or (com == 2 and my == 0): 
            strWinner = "나의 승리!"
            intRes = 1
        else:
            strWinner = "컴퓨터의 승리!"
            intRes = 2

    # 출력
    print("컴퓨터: "+strCom)
    print(str(time) + " 번째 판 " + strWinner)
    print("#################################")
    
    return intRes
    
# 사용자의 입력을 받는 함수
def userRsp() : 
    try :
        deci = input("나: ")
        my = int(deci)
        if my > 2 : 
            print("잘못 입력했습니다. 0,1,2 중에 입력해주세요")
            return userRsp()
        return my
    except : 
        if deci == "가위" : 
            my = 0
        elif deci == "바위" : 
            my = 1
        elif deci == "보" : 
            my = 2
        else :
            print("잘못 입력했습니다. 가위,바위,보 중에 입력해주세요")
            return userRsp()
        return my

# convertNumToRsp(num) : 숫자 인자를 받아 문자(가위,바위,보)로 변환시키는 함수
def convertNumToRsp(num):
    rsp = ''
    if num == 0 :
        rsp = '가위'
    elif num == 1 : 
        rsp = '바위'
    elif num == 2 : 
        rsp = '보'
    return rsp

def rsp_advanced(times) : 
    i = 0
    intDrawCnt = 0 
    intMyWinCnt = 0
    intComWinCnt = 0
    
    while i < times : 
        print("가위 바위 보 : " + str(i))
        i += 1
        res = rspWinner(i)
        if res == 0 : 
            intDrawCnt += 1
        elif res == 1 : 
            intMyWinCnt += 1
        elif res == 2 :
            intComWinCnt += 1
    
    #전적을 출력하기
    print("############게임결과############")
    print("나의 전적:",str(intMyWinCnt)+"승",str(intDrawCnt)+"무",str(intComWinCnt)+"패")
    print("컴퓨터의 전적:",str(intComWinCnt)+"승",str(intDrawCnt)+"무",str(intMyWinCnt)+"패")
        
# 출력하기
try : 
    games = int(input("몇 판을 진행하시겠습니까?:"))
    rsp_advanced(games)
except : 
    print("판수는 숫자만 입력 가능합니다")
