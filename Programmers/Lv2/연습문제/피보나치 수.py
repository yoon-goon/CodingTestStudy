# https://school.programmers.co.kr/learn/courses/30/lessons/12945


def solution(n):
    current, nextnum = 0, 1
    for i in range(n):
        current, nextnum = nextnum, current + nextnum # 2 계산이 동시에 이뤄저야 하므로 ,로 같은줄에 작성
    return current


print(solution(3))
print(solution(5))
