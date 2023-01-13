# https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = ''
    count = 1
    while n >= 3:
        n = n - 3 ** count
        count += 1
        if n % 3 == 0:
            answer = answer + "0"
        else:
            answer = answer + "1"
    return answer


print(solution(45))
