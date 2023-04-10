# 함수를 이용해 간략화 시키기


membership = input("회원 등급 입력: ")
parkingTime = int(input("주차 시간 입력: "))
print(f"회원 등급: {membership}")
print(f"주차 시간: {parkingTime}")
if membership == "플래티넘" or membership == "골드":
    if parkingTime > 120:
        fee = (parkingTime - 120) // 10 * 1000
        print(f"주차 요금: {fee}원")
    else: # if parkingTime <= 120:
        print("주차 요금 0원")
elif membership == "실버" or membership == "프렌즈":
    purchased = int(input("구매 금액 입력: "))
    if purchased >= 30000:
        if parkingTime > 120:
            fee = (parkingTime - 120) // 10 * 1000
            print(f"주차 요금: {fee}원")
        else: # if parkingTime <= 120:
            print("주차 요금 0원")
    elif purchased >= 10000:
        if parkingTime > 60:
            fee = (parkingTime - 60) // 10 * 1000
            print(f"주차 요금: {fee}원")
        else: # if parkingTime <= 60:
            print("주차 요금 0원")
    else:
        fee = parkingTime // 10 * 1000
        print(f"주차 요금: {fee}원")
elif membership == "비회원":
    purchased = int(input("구매 금액 입력: "))
    if purchased >= 50000:
        if parkingTime > 120:
            fee = (parkingTime - 120) // 10 * 1000
            print(f"주차 요금: {fee}원")
        else: # if parkingTime <= 120:
            print("주차 요금 0원")
    elif purchased >= 30000:
        if parkingTime > 60:
            fee = (parkingTime - 60) // 10 * 1000
            print(f"주차 요금: {fee}원")
        else: # if parkingTime <= 60:
            print("주차 요금 0원")
    else:
        fee = parkingTime // 10 * 1000
        print(f"주차 요금: {fee}원")