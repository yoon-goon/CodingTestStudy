# 함수를 이용해 간략화 시키기
def over120(time):
    if time > 120:
        fee = (time - 120) // 10 * 1000
        print(f"주차 요금: {fee}원")
    else:
        print("주차 요금 0원")


def over60(time):
    if time > 60:
        fee = (time - 60) // 10 * 1000
        print(f"주차 요금: {fee}원")
    else:
        print("주차 요금 0원")


def else10(time):
    fee = time // 10 * 1000
    print(f"주차 요금: {fee}원")


membership = input("회원 등급 입력: ")
parkingTime = int(input("주차 시간 입력: "))
print(f"회원 등급: {membership}")
print(f"주차 시간: {parkingTime}")
if membership == "플래티넘" or membership == "골드":
    over120(parkingTime)
elif membership == "실버" or membership == "프렌즈":
    purchased = int(input("구매 금액 입력: "))
    if purchased >= 30000:
        over120(parkingTime)
    elif purchased >= 10000:
        over60(parkingTime)
    else:
        else10(parkingTime)

elif membership == "비회원":
    purchased = int(input("구매 금액 입력: "))
    if purchased >= 50000:
        over120(parkingTime)
    elif purchased >= 30000:
        if parkingTime > 60:
            over60(parkingTime)
    else:
        else10(parkingTime)
