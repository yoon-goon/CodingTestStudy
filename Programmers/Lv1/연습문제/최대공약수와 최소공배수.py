# https://school.programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []
    arr1 = []
    arr2 = []
    for i in range(1, n + 1):  # 공약수를 구하는 과정
        if n % i == 0:
            arr1.append(i)
    for y in range(1, m + 1):
        if m % y == 0:
            arr2.append(y)
    for x in arr1:
        if x in arr2:
            answer.append(x)
    answer.remove(1)

    for i in range(1, 1000001):  # 공배수를 구하는 과정
        if i % n == 0 and i % m == 0:
            answer.append(i)
            return answer
    return answer


print(solution(3, 12))
