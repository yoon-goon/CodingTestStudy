# https://school.programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    answer = ''
    for i in range(len(n)):
        if i%2 != 0:
            answer.append("수")
        else:
            answer.append("박")
    return answer

