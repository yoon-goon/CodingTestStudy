# https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    alist = list(str(n))
    alist.sort()
    answer = int("".join(alist[::-1]))
    return answer


print(solution(118372))
