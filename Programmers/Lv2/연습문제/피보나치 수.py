# https://school.programmers.co.kr/learn/courses/30/lessons/12945


def solution(n):
    current, next = 0, 1
    for i in range(n):
        current, next = next, current + next
    return current


print(solution(3))
print(solution(5))
