print("사용자의 회원등급을 입력해 주세요.")
A = str(input())
print("주차 시간(분)을 입력해 주세요.")
B = int(input())

money = 0

if A == "실버" or A == "프렌즈" or A == "비회원":
    print("구매 금액을 입력해주세요.")
    C = int(input())
    if A == "실버" or A == "프렌즈":
        if C >= 30000:
            money = (B - 120) // 10 * 1000
        elif C >= 10000:
            money = (B - 60) // 10 * 1000
        else:
            money = B // 10 * 1000

else:
    money = (B - 120) // 10 * 1000

print(f"주차요금은 {money}원 입니다.")
