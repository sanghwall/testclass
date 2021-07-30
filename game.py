import random
while True:
    컴퓨터 = random.randint(1,3)
    user = int(input('가위바위보를 내세요: '))
    if 컴퓨터 == user:
        print('비겼습니다. 다시 시도하세요.')
    elif 컴퓨터 == 1 and user == 3:
        print('컴퓨터가 이겼습니다. 다시 시도하세요.')
    elif 컴퓨터 == 2 and user == (1):
        print('컴퓨터가 이겼습니다. 다시 시도하세요.')
    elif 컴퓨터 == 3 and user == 2:
        print('컴퓨터가 이겼습니다. 다시 시도하세요.')
    elif 컴퓨터 == 1 and user == 2:
        print('당신이 이겼습니다.') 
        break
    elif 컴퓨터 == 2 and user == 3:
        print('당신이 이겼습니다.') 
        break
    elif 컴퓨터 == 3 and user == 1:
        print('당신이 이겼습니다.')
        break
