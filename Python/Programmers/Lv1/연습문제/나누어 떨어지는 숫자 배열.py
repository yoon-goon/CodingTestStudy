# https://school.programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    arr.sort()
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if answer == []:
        return [-1]
    return answer


print(solution([5, 9, 7, 10], 5))
