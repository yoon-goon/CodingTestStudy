# https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for y in numbers[i+1:]:
            if not numbers[i]+y in answer:
                answer.append(numbers[i] + y)

    return sorted(answer)


print(solution([2, 1, 3, 4, 1]))
