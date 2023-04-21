'''
 컴퓨터와 사람의 주사위 던지기
 컴퓨터는 무작위 숫자 발생기를 이용해서 주사위를 굴리
는 것과 같은 효과를 내도록 함
 사람은 원하는 숫자를 입력
 두 개를 비교해서 누가 이겼는지 화면에 출력
 사람이 입력한 숫자가 1-6사이가 아니면 오류 출력
'''

import random

cpu = random.randint(1, 6)

human = int(input())
if human < 1 or human > 6:
    print("주사위 이상 값 입력 오류!")
else:
    if cpu > human:
        print("컴퓨터 승리!:", cpu)
    elif cpu == human:
        print("비김!", cpu)
    elif cpu < human:
        print("사용자승리!", human)
