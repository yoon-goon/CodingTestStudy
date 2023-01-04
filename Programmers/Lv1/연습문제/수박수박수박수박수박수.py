# https://school.programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    answer = ''
    for i in range(1, n + 1):
        if i % 2 != 0:
            answer = answer + ("수")
        else:
            answer = answer + "박"
    return answer


def solution2(n):
    return "수박" * (n // 2) + "수" * (n % 2)


print(solution(3))
print(solution2(3))
print(solution2(4))
