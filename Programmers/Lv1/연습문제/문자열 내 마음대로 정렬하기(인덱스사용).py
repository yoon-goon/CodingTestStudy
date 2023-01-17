# https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    arr = []
    answer = []
    for i in strings:
        arr.append(i[n]+i)
    arr.sort()
    for i in arr:
        answer.append(i[1:])

    return answer




print(solution(["sun", "bed", "car"], 1))
