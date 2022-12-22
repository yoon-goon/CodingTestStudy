# https://school.programmers.co.kr/learn/courses/30/lessons/142086
''' 완전 오답, 문제 이해를 잘못함
def solution(s):
    answer = []
    newarr = []
    for i in range(len(s)):
        if s[i] in newarr:
            answer.append(2)
        else:
            answer.append(-1)
        newarr.append(s[i])

    return answer
'''


def solution(s):
    answer = []
    return answer


print(solution("banana"))
print(solution("foobar"))
