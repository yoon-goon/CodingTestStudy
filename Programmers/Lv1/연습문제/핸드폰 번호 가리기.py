# https://school.programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    backF = phone_number[-4:] 
    return "*" * (len(phone_number) - 4) + backF

print(solution("01033334444"))
