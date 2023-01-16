# https://school.programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = []
    if n >= 2:
        answer.append(2)

    for i in range(1, n + 1):
        for y in range(i-1, 1,-1):
            if i % y == 0:
                break;




    return answer


print(solution(10))
print(solution(5))
