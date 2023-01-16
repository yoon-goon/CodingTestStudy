# https://school.programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = []
    if n >= 2:
        answer.append(2)

    for i in range(1, n + 1):
        for y in range(2, i):
            if i % y == 0:
                break

        answer.append(i)

    return answer


print(solution(10))
print(solution(5))
