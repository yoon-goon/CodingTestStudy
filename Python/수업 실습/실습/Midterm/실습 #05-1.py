# Same as 실습 #03-2

import random

cpu = random.randint(1, 6)


human = int(input())

if not 1 <= human <= 6:
    print("오류 1-6사이 값을 입력하세요")
else:
    print("컴퓨터의 주사위:", cpu)
    print("사용자의 주사위:", human)
    if cpu > human:
        print("컴퓨터 승리!:", cpu)
    elif cpu == human:
        print("비김!", cpu)
    elif cpu < human:
        print("사용자승리!", human)



# import random
#
# computer = random.randint(1,6)
#
# human = int(input("1부터 6까지의 정수값을 입력하세요"))
# if not 1 <= human <= 6:
#
# print(f"cpu:{computer}")
# print(f"Human:{human}")
