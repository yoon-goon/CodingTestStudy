# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = s.replace(" ","")

    return print(min(answer)+" "+max(answer))

print(solution("1 2 3 4"))