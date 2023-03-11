# https://school.programmers.co.kr/learn/courses/30/lessons/142086


def solution(s):
    answer = []
    dic1 = dict()
    for i in range(len(s)):
        if s[i] in dic1:
            answer.append(i - dic1[s[i]])
        else:
            answer.append(-1)  # 이전에 없던 글자면 -1
        dic1[s[i]] = i
    return answer


print(solution("banana"))
print(solution("foobar"))

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
