# https://school.programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    backF = phone_number[-4:] # 뒷 4자리만 저장
    return "*" * (len(phone_number) - 4) + backF # 번호 길이에서 4 뺀뒤 뒷 4자리를 더함

print(solution("01033334444"))
