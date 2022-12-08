#https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    total = 0
    for i in range(count):
        total += price * (i + 1)
    if money > total:
        return 0
    answer = money - total

    return abs(answer)

print(solution(3, 20, 4))