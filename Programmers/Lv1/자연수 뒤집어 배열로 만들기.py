# https://school.programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    X = [int(i) for i in str(n)]
    return X[::-1]


print(solution(12345))


# 다른풀이
def Altsolution(n):
    answer = []

    while n > 1:
        answer.append(int(n % 10)) #12345 -> .append(5) , #1234 -> .append(4)
        n /= 10 # 12345 -> 1234

    return answer


print(Altsolution(12345))
