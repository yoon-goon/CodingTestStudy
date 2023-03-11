# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    total = 0
    for i in range(count):
        total += price * (i + 1)  # i가 0부터 시작하기 때문에 +1
    if money > total:  # 문제 조건에 돈이 부족하지 않은 경우 0을 출력하도록 되어있어 if문으로 구현
        return 0
    answer = money - total

    return abs(answer)


print(solution(3, 20, 4))
