# https://school.programmers.co.kr/learn/courses/30/lessons/12943
def solution(num):
    count = 0
    while num != 1:
        count += 1
        if count == 500:
            return -1
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
    return count

print(solution(6))
print(solution(16))
print(solution(626331))
