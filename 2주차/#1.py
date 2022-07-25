import random

#오프닝
print('Do you wanna play 가위바위보?')
computer = random.choice(['가위','바위','보'])
player = input('가위 바위 보 중 하나를 입력해봐:')

#만약 컴퓨터가 가위를 냈다면
if computer == '가위':
    print('컴퓨터: 가위')
    if player == '가위':
        print('플레이어: 가위')
        print('컴퓨터: 아.. 무승부네')
    elif player == '바위':
        print('플레이어: 바위')
        print('컴퓨터: 이런 내가 지다니.. 다시 한판 해')
    elif player == '보':
        print('플레이어: 보')
        print('컴퓨터: 하하하.. 나의 승리다. 다 이겨주마')

#만약 컴퓨터가 바위를 냈다면
elif computer == '바위':
    print('컴퓨터: 바위')
    if player == '가위':
        print('플레이어: 가위')
        print('컴퓨터: 하하하.. 나의 승리다. 남자는 바위지')
    elif player == '바위':
        print('플레이어: 바위')
        print('컴퓨터: 아.. 무승부네. 따라하지마')
    elif player == '보':
        print('플레이어: 보')
        print('컴퓨터: 이런 내가 지다니.. 실수다')
        
#만약 컴퓨터가 보를 냈다면
elif computer == '보':
    print('컴퓨터: 보')
    if player == '가위':
        print('플레이어: 가위')
        print('컴퓨터: 이런 내가 지다니.. 운이 좋았군')
    elif player == '바위':
        print('플레이어: 바위')
        print('컴퓨터: 하하하.. 나의 승리다. 너의 패배군')
    elif player == '보':
        print('플레이어: 보')
        print('컴퓨터: 아.. 무승부라니 납득할 수 없군')
        
