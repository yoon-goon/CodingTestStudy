# https://school.programmers.co.kr/learn/courses/30/lessons/120830

def solution(n, k):
    sheepstick = n * 12000
    drink = k * 2000
    serv = (n // 10) * 2000

    return sheepstick + drink - serv


# 입출력 코드
print(solution(10, 3))
print(solution(64, 6))
