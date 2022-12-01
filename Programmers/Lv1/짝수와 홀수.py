# https://school.programmers.co.kr/learn/courses/30/lessons/12937
'''
def solution(num):
    answer = ''
    if num//2 == 1 or num//2 == -1:
        answer = 'Odd'
    else:
        answer = 'Even'
    print(answer)
    return answer#
    '''  # 예시 입출력 테스트는 통과했으나 채점에서 문제발생


def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    print(answer)
    return answer


solution(3)
solution(4)
solution(-1)
