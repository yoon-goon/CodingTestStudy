# https://school.programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = []
    count = 0
    for i in range(1, n + 1):
        for y in range(i, 1, -1):
            if i % y == 0:
                count += 1
        if count == 1:
            answer.append(i)
        count = 0

    return len(answer)


print(solution(10))
print(solution(7))
print(solution(5))
