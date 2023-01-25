# https://school.programmers.co.kr/learn/courses/30/lessons/12945


def solution(n):
    current, nextnum = 0, 1
    for i in range(n):
        current, nextnum = nextnum, current + nextnum
    return current


print(solution(3))
print(solution(5))
