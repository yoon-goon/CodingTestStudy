# https://school.programmers.co.kr/learn/courses/30/lessons/12912


def solution(a, b):
    answer = 0
    if a <= b:  # b가 a보다 커서 for문이 의도와 다르게 작동하는걸 수정하기 위함
        x = a
        y = b
    else:
        x = b
        y = a
    for i in range(x, y + 1):
        answer += i
    return answer


print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))
