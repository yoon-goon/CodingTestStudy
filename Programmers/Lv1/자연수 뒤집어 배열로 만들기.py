# https://school.programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    X = [int(i) for i in str(n)]
    return X[::-1]


print(solution(12345))


